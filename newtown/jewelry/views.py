from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max, Min
from .models import *
#need to write generic view for specific metals and for specific materials
def index(request):
	return render(request,'jewelry/jewelry_root.html',{''})
def metals(request):
	metal_choices = Metal.METAL_CHOICES
	jewelry_items= Metal.objects.all()
	price_range = [jewelry_items.aggregate(Min('price')),jewelry_items.aggregate(Max('price'))]
	size_range = [jewelry_items.aggregate(Min('size')),jewelry_items.aggregate(Max('size'))]
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
'''
def gold(request):
	jewelry_items = Jewelry.objects.filter(metal = 'Gold')
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
def silver(request):
	jewelry_items = Jewelry.objects.filter(metal = 'Silver')
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
def bronze(request):
	jewelry_items = Jewelry.objects.filter(metal = 'Bronze')
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
def steel(request):
	jewelry_items = Jewelry.objects.filter(metal = 'Steel')
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
'''
