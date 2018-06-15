from .models import *
from .forms import EmailForm

def email_signup(request):
	return {'email_form':EmailForm()}	
