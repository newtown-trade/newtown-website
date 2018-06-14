from django.shortcuts import render
from django.http import HttpResponse
from jewelry.models import *

def index(request):
	metal_latest = Metal.objects.order_by('-timestamp')[:3]
	contactLense_latest = ContactLense.objects.order_by('-timestamp')[:3]
	return render(request,'newtown/home.html',{'metal_latest':metal_latest,'contactLense_latest':contactLense_latest})
