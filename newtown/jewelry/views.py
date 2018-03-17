from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
	all_jewelry = Jewelry.objects.all()
	return render(request, 'jewelry/jewelry_list.html',{'all_jewelry':all_jewelry})
def gold(request):
	gold_jewelry = Jewelry.objects.filter(metal = 'Gold')
# Create your views here.
