from django.shortcuts import render
from django.http import HttpResponse
from jewelry.models import *
import jewelry.models as jewelry_models
import inspect

def index(request):
	metal_latest = Metal.objects.order_by('-timestamp')[:3]
	contactLense_latest = ContactLense.objects.order_by('-timestamp')[:3]

	#gets list of types of jewelry and its style type
	jewelry_classes={}
	for name,obj in inspect.getmembers(jewelry_models):
		if inspect.isclass(obj) and obj.__name__ not in ['Display','Side']:
			jewelry_classes[obj._meta.verbose_name]=[obj.objects.values_list(obj.style,flat=True),obj.__name__,obj]
			print(obj.style)
	return render(request,'newtown/home.html',{'metal_latest':metal_latest,'contactLense_latest':contactLense_latest,'jewelry_classes':jewelry_classes})
