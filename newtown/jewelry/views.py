from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.db.models import Max, Min
from django.urls import reverse
from .models import *
from .class_parser import *

#need to write generic view for specific metals and for specific materials

#given a Model's raw get_field result, its name par apps.py, its specific method, and the display name from the admin, returns the required context
def generate_context(get_field_result,model_name,specific_method,display_name):

	#parses out and obtains field types
	attributes = {}
	for i in get_field_result:
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField','DateTimeField']:
			attributes[i.name]=[i.verbose_name,str(i.get_internal_type())]

	#generates the item-specific urls
	specific_url = (reverse('jewelry:'+specific_method,args=[model_name,177013,1337]).replace('1337','{{objectID}}')).replace('177013','{{jewelry_style}}')
	print(specific_url)

	#returns the context to be fed into the view
	return {'specific_url':specific_url,'model_name':model_name,'attributes':attributes, 'display_name':display_name}

#WARNING: code will change if multiple images
#given a specific item requested via pk and a url back to the full list, dynamically generates a profile for item and returns context
#url_to_full_list (i.e. the link back to object type's list (e.g. metals) is generated here to abstract it from the template
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

def index(request):
	return render(request,'jewelry/jewelry_root.html',{})

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

def display(request):
	return render(request,'jewelry/display.html',generate_context(Display._meta.get_fields(),Display.__name__,'displaySpecific',Display._meta.verbose_name_plural))
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
	if obj is not None:
		jewelry_item = get_object_or_404(obj,pk=jewelry_id,jewelry_style=jewelry_style_user)
		return render(request,'jewelry/style_specific.html',{'jewelry_item':jewelry_item,'jewelry_type':jewelry_type,'jewelry_style_user':jewelry_style_user,'jewelry_display_name':obj._meta.verbose_name})
	return HttpResponse('Invalid Option')

#A generalized search method that implements the new Dynamic URL Construction method
#Invokes generate_context, but replaces get_specific_item with style_specific. (Mainly due to incompabilities with URL)
def search(request,jewelry_type):
	obj = class_parser(jewelry_type)
	if obj is not None:
		return render(request,'jewelry/jewelry_list.html',generate_context(obj._meta.get_fields(),obj.__name__,'style_specific',obj._meta.verbose_name_plural))
	raise Http404("Style does not Exist")
