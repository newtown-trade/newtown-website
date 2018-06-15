from django.utils import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *

#output from contact us
#TODO: make this an actual template lol
def contact_submit(request):
	return render(request,'contact/contact_reciept.html',{})

#view for Contact Us
def index(request):
	#checks if form submission
	if request.method=='POST':
		form = ContactForm(request.POST)
		#checks if form is valid, and does other stuff
		if form.is_valid():
			contact = form.save(commit=False)
			contact.timestamp=timezone.now()
			contact.save()
			#constructs and sends email to email
			#TODO: set up mail server + make actual email newtown0312@
			send_mail('[MESSAGE FROM \'CONTACT US\']: ' + contact.title,contact.message,contact.email,['leebr1@bxscience.edu'])
			return redirect('contact:contact_submit')
	else:
		form = ContactForm()
	return render(request,'contact/contact_form.html',{'form':form})

#form processor for email signups
def email_signup(request):
	if request.method == 'POST':
		email_signup = EmailForm(request.POST)
		if email_signup.is_valid():
			email = email_signup.save(commit=False)
			email.timestamp = timezone.now()
			email.save()
			print('saved!')
	else:
		email_form=EmailForm()
	return redirect('contact:contact_submit')
