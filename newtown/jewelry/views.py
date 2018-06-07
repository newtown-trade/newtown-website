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
		if i.get_internal_type() in ['ManyToManyField','AutoField','FileField','ImageField']:
			pass
		else:
			attributes[i.name]=[i.verbose_name,str(i.get_internal_type())]

	#generates the item-specific urls
	specific_url = reverse('jewelry:'+specific_method,args=[1337]).replace('1337','{{objectID}}')

	#returns the context to be fed into the view
	return {'specific_url':specific_url,'model_name':model_name,'attributes':attributes}

def index(request):
	return render(request,'jewelry/jewelry_root.html',{})

def metals(request):
	#legacy code kept in case something breaks
	'''
	#gets attributes of Metal's fields that are indexable under Algolia, such that Algolia's search parameters can be generated
	attributes = {}
	for i in Metal._meta.get_fields():
		if i.get_internal_type() in ['ManyToManyField','AutoField','FileField','ImageField']:
			pass
		else:
			attributes[i.name] = [i.verbose_name,str(i.get_internal_type())]	
	print(attributes)

	#pre-generates a url to create specific links for Algolia's objects:	
	metal_specific_url=reverse('jewelry:metal_specific',args=[1337]).replace('1337','{{objectID}}') #1337 is arbitrary
	model_name=Metal.__name__
	'''

	return render(request,'jewelry/metal.html',generate_context(Metal._meta.get_fields(),Metal.__name__,'metal_specific'))
	#return render(request, 'jewelry/jewelry_list.html',{'metal_url_specific':metal_specific_url,'model_name':model_name,'attributes':attributes}) 
def metal_specific(request,metal_id):
	metal_jewelry = get_object_or_404(Metal,pk=metal_id)
	return render(request,'jewelry/jewelry_specific.html',{metal_jewelry:'metal_jewelry'})
def display(request):
	displays = Display.objects.all()
	return render(request,'jewelry/display_temp.html')#this will be superseded by a generic view later

