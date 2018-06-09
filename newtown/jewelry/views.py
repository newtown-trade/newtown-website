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

def index(request):
	return render(request,'jewelry/jewelry_root.html',{})

def metals(request):
	#legacy code kept in case something breaks

	return render(request,'jewelry/metal.html',generate_context(Metal._meta.get_fields(),Metal.__name__,'metal_specific'))
	#return render(request, 'jewelry/jewelry_list.html',{'metal_url_specific':metal_specific_url,'model_name':model_name,'attributes':attributes}) 

def metal_specific(request,metal_id):

	#gets the Algolia-Indexable attributes of an object and dynamically grabs them to be displayed
	#note: this section doesn't actually use Algolia
	specific_item = get_object_or_404(Metal,pk=metal_id)
	item_attributes = {}
	for i in specific_item._meta.get_fields():
		if i.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField']:		
			item_attributes[str(i.verbose_name)]=str(getattr(specific_item,str(i.name)))
	print(item_attributes)

	#gets url to return back to full list of objects	
	url_to_full_list = reverse('jewelry:metals')

	#TODO: fix 'unhashable type: dict bug'
	return render(request,'jewelry/jewelry_specific.html',{specific_item:'specific_item',url_to_full_list:'url_to_full_list',item_attributes:'item_attributes'})

def contactLense(request):
	return HttpResponse('test for contact lense')
def contactLenseSpecific(request,contactLense_id):
	contact_lense_specific = get_object_or_404(ContactLense,pk=contactLense_id)
	return HttpResponse(contact_lense_specific.color)	

def display(request):
	displays = Display.objects.all()
	return render(request,'jewelry/display_temp.html')#this will be superseded by a generic view later

