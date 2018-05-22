from django.conf.urls import url, include

from . import views

urlpatterns = [#need to write generic view for specific metals and for specific materials
	url(r'^$',views.index,name='index'),
	url(r'^metal/$',views.metals,name='metals'),
	#url(r'^gold/$',views.gold, name='gold'),
	#url(r'^silver/$',views.silver, name='silver'),
	#url(r'^bronze/$',views.bronze, name='bronze'),
	#url(r'^steel/$',views.steel, name='steel'),


]
