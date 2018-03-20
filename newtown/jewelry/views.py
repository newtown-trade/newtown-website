from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#need to write generic view for specific metals and for specific materials
def index(request):
	jewelry_items= Jewelry.objects.all()
	print(len(jewelry_items))
	return render(request, 'jewelry/jewelry_list.html',{'jewelry_items':jewelry_items})
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
