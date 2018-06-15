from django.conf.urls import url

from . import views
app_name='contact'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^submit/$',views.contact_submit,name='contact_submit'),
	url(r'^email_signup/$',views.email_signup,name='email_signup')
]
