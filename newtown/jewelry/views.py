from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Max, Min
from django.urls import reverse
from .models import *
#need to write generic view for specific metals and for specific materials
def index(request):
	return render(request,'jewelry/jewelry_root.html',{})
def metals(request):
	metal_choices = Metal.METAL_CHOICES
	jewelry_items= Metal.objects.all()
	#price_range = [jewelry_items.aggregate(Min('price')),jewelry_items.aggregate(Max('price'))]
	#size_range = [jewelry_items.aggregate(Min('size')),jewelry_items.aggregate(Max('size'))]

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

	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items,'metal_url_specific':metal_specific_url}) 
def metal_specific(request,metal_id):
	metal_jewelry = get_object_or_404(Metal,pk=metal_id)
	return render(request,'jewelry/jewelry_specific.html',{metal_jewelry:'metal_jewelry'})
def display(request):
	displays = Display.objects.all()
	return render(request,'jewelry/display_temp.html')#this will be superseded by a generic view later

