from django.utils import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

def contact_submit(request):
	return HttpResponse("tha")

#view for Contact Us
def index(request):
	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.timestamp=timezone.now()
			contact.save()
			return redirect('contact_submit')
	else:
		form = ContactForm()
	return render(request,'contact/contact_form.html',{'form':form})
# Create your views here.
