from django.shortcuts import render
from django.http import HttpResponse
from jewelry.models import *
import jewelry.models as jewelry_models
import inspect

def index(request):

	#grabs 3 most recent entries under ContactLense and Metal
	metal_latest = Metal.objects.order_by('-timestamp')[:3]
	contactLense_latest = ContactLense.objects.order_by('-timestamp')[:3]
	#generate template
	return render(request,'newtown/home.html',{'metal_latest':metal_latest,'contactLense_latest':contactLense_latest})
