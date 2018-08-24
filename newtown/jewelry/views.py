from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.db.models import Max, Min
from django.urls import reverse
from .models import *
from .class_parser import *


#returns root directory for jewelry app
def index(request):
	return render(request,'jewelry/jewelry_root.html',{})

#given a Model's raw get_field result, its name par apps.py, its specific method, and the display name from the admin, returns the required context
def generate_context(get_field_result,model_name,specific_method,display_name,replace_parameters):

	#parses out and obtains field types
	attributes = {}
	for i in get_field_result:
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField','DateTimeField']:
			attributes[i.name]=[i.verbose_name,str(i.get_internal_type())]

	#specific_url = reverse('jewelry:'+specific_method,args=list(replace_parameters.keys()))
	#specific_url=reverse('jewelry:'+specific_method,kwargs=replace_parameters)
	#specific_url = (reverse('jewelry:'+specific_method,args=[model_name,177013,1337]).replace('1337','{{objectID}}')).replace('177013','{{jewelry_style}}')

	#generates template for specific jewelry that algolia later uses
	#due to problems with reverse(), link is handmade.
	specific_url = '/jewelry'
	for key, value in replace_parameters.items():
		specific_url = specific_url + '/' + key
		specific_url=specific_url.replace(key,value)

	#returns the context to be fed into the view
	return {'specific_url':specific_url,'model_name':model_name,'attributes':attributes, 'display_name':display_name}

#WARNING: code will change if multiple images
#given a specific item requested via pk and a url back to the full list, dynamically generates a profile for item and returns context
#url_to_full_list (i.e. the link back to object type's list (e.g. metals) is generated here to abstract it from the template
#the only class that implements this technqiue is Display
def get_specific_item(specific_item, url_to_full_list):

	#grabs the object's fields and values
	#note: different dictionary structure than generate_context
	item_attributes = {}
	image_url=''

	for i in specific_item._meta.get_fields():
		#grabs value for majority of indexable fields
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField','DateTimeField']:		
			item_attributes[str(i.verbose_name)]=str(getattr(specific_item,str(i.name)))
		#separately grabs URL to image and pipes it to optional entry in context
		elif i.get_internal_type() in ['FileField','ImageField']:
			image_url=getattr(getattr(specific_item,str(i.name)),'url')
		#code to catch ManyToManyFields
		#implement this in v0.6
		#elif i.get_internal_type() == 'ManyToManyField':
			#print(i.get_internal_type())

	#compiles context to return and optionally stacks image on top
	attributes={'specific_item':specific_item,'url_to_full_list':url_to_full_list,'item_attributes':item_attributes}
	if len(image_url)>0:
		attributes['image_url']=image_url
	#return context to be fed back to view
	return attributes

#view functions for Display
#NOTE: because Display doesn't have jewelry_style, cannot use style/style_specific generalized methods

def display(request):
	return render(request,'jewelry/display.html',generate_context(Display._meta.get_fields(),Display.__name__,'displaySpecific',Display._meta.verbose_name_plural,{'display':'display','1337':'{{objectID}}'}))
def displaySpecific(request,display_id):
	return render(request,'jewelry/jewelry_specific.html',get_specific_item(get_object_or_404(Display,pk=display_id),reverse('jewelry:display')))

#generalized view for displaying all jewelry of a certain jewelry type's style
#determines if a class in models.py is a) not Display and b) is the right jewelry
#jewelry_style is standard on the database level, so that doesn't need to be automated
def style(request,jewelry_type,jewelry_style_user):

	#parses out the appropriate Model -- see class_parser.py
	obj = class_parser(jewelry_type)
	if obj is not None:
		jewelry_queryset = obj.objects.filter(jewelry_style=jewelry_style_user)
		if len(jewelry_queryset)>0:
			return render(request,'jewelry/style_list.html',{'jewelry_queryset':jewelry_queryset,'jewelry_display_name':obj._meta.verbose_name,'jewelry_style_user':jewelry_style_user,'jewelry_type':jewelry_type})

	#todo: insert generic template here
	raise Http404("Style does not Exist")

#given a requested jewelry type AND its corresponding style, pulls (or fails to) pull an appropriate object from DB
def style_specific(request, jewelry_type, jewelry_style_user,jewelry_id):

	#parses out appropriate Model -- see class_parser.py
	obj = class_parser(jewelry_type)

	#assuming object is not one, generates context using get_specific_item, creates in-house context, and returns meshed together option
	if obj is not None:
		jewelry_item = get_object_or_404(obj,pk=jewelry_id,jewelry_style=jewelry_style_user)
		context_from_method = get_specific_item(jewelry_item,'')
		context_inhouse={'jewelry_type':jewelry_type,'jewelry_style_user':jewelry_style_user,'jewelry_display_name':obj._meta.verbose_name}
		context = {**context_from_method,**context_inhouse}
		return render(request,'jewelry/style_specific.html',context)

	#error 404
	return Http404('Item Does Not Exist')

#A generalized search method that implements the new Dynamic URL Construction method
#also doubles as subhome screen
#Invokes generate_context, but replaces get_specific_item with style_specific. (Mainly due to incompabilities with URL)
def search(request,jewelry_type):
	print(jewelry_type)
	obj = class_parser(jewelry_type)
	if obj is not None:
		styles=obj.objects.values_list('jewelry_style',flat=True)
		context=generate_context(obj._meta.get_fields(),obj.__name__,'style_specific',obj._meta.verbose_name_plural,{'jewelry_type':obj.__name__,'jewelry_style_user':'{{ jewelry_style }}','jewelry_id':'{{objectID}}'})
		context['styles']=styles
		return render(request,'jewelry/jewelry_list.html',context)
	raise Http404("Style does not Exist")

'''
def metals(request):
	return render(request,'jewelry/metal.html',generate_context(Metal._meta.get_fields(),Metal.__name__,'metal_specific',Metal._meta.verbose_name_plural))
	#return render(request, 'jewelry/jewelry_list.html',{'metal_url_specific':metal_specific_url,'model_name':model_name,'attributes':attributes}) 

def metal_specific(request,metal_id):
	return render(request,'jewelry/jewelry_specific.html',get_specific_item(get_object_or_404(Metal,pk=metal_id),reverse('jewelry:metals'))) #see comments for get_specific_item

def contactLense(request):
	return render(request,'jewelry/contactLense.html',generate_context(ContactLense._meta.get_fields(),ContactLense.__name__,'contactLenseSpecific',ContactLense._meta.verbose_name_plural))
def contactLenseSpecific(request,contactLense_id):
	return render(request,'jewelry/jewelry_specific.html',get_specific_item(get_object_or_404(ContactLense,pk=contactLense_id),reverse('jewelry:contactLense')))
'''

