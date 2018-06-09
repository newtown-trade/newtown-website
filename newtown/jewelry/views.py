from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Max, Min
from django.urls import reverse
from .models import *
#need to write generic view for specific metals and for specific materials

#given a Model's raw get_field result, its name par apps.py and its specific method, returns the required context
def generate_context(get_field_result,model_name,specific_method):

	#parses out and obtains field types
	attributes = {}
	for i in get_field_result:
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField']:
			attributes[i.name]=[i.verbose_name,str(i.get_internal_type())]

	#generates the item-specific urls
	specific_url = reverse('jewelry:'+specific_method,args=[1337]).replace('1337','{{objectID}}')

	#returns the context to be fed into the view
	return {'specific_url':specific_url,'model_name':model_name,'attributes':attributes}

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
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField']:		
			item_attributes[str(i.verbose_name)]=str(getattr(specific_item,str(i.name)))
		#separately grabs URL to image and pipes it to optional entry in context
		elif i.get_internal_type() in ['FileField','ImageField']:
			image_url=getattr(getattr(specific_item,str(i.name)),'url')

	#compiles context to return and optionally stacks image on top
	attributes={'specific_item':specific_item,'url_to_full_list':url_to_full_list,'item_attributes':item_attributes}
	if len(image_url)>0:
		attributes['image_url']=image_url
	#return context to be fed back to view
	return attributes

def index(request):
	return render(request,'jewelry/jewelry_root.html',{})

def metals(request):
	return render(request,'jewelry/metal.html',generate_context(Metal._meta.get_fields(),Metal.__name__,'metal_specific'))
	#return render(request, 'jewelry/jewelry_list.html',{'metal_url_specific':metal_specific_url,'model_name':model_name,'attributes':attributes}) 

def metal_specific(request,metal_id):
	return render(request,'jewelry/jewelry_specific.html',get_specific_item(get_object_or_404(Metal,pk=metal_id),reverse('jewelry:metals'))) #see comments for get_specific_item

def contactLense(request):
	return render(request,'jewelry/contactLense.html',generate_context(ContactLense._meta.get_fields(),ContactLense.__name__,'contactLenseSpecific'))
def contactLenseSpecific(request,contactLense_id):
	return render(request,'jewelry/jewelry_specific.html',get_specific_item(get_object_or_404(ContactLense,pk=contactLense_id),reverse('jewelry:contactLense')))

def display(request):
	displays = Display.objects.all()
	return render(request,'jewelry/display_temp.html')#this will be superseded by a generic view later

