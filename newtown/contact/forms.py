from django import forms

from .models import *

#form for contact us form
class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=('name','email','title','message')

#form for email signups
class EmailForm(forms.ModelForm):
	class Meta:
		model=EmailResponse
		fields = ('email',)
