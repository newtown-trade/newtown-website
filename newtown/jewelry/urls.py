from django.conf.urls import url, include

from . import views
app_name='jewelry'
urlpatterns = [#need to write generic view for specific metals and for specific materials
	url(r'^$',views.index,name='index'),
	url(r'^metals/$',views.metals,name='metals'),
	url(r'^metals/(?P<metal_id>[0-9]+)/$',views.metal_specific, name = "metal_specific"),
	url(r'^display/$',views.display,name="display"),
	url(r'^display/(?P<display_id>[0-9]+)/$',views.displaySpecific,name="displaySpecific"),
	url(r'^contactLense/$',views.contactLense,name="contactLense"),
	url(r'^contactLense/(?P<contactLense_id>[0-9]+)/$',views.contactLenseSpecific,name="contactLenseSpecific"),
	#url(r'^silver/$',views.silver, name='silver'),
	#url(r'^bronze/$',views.bronze, name='bronze'),
	#url(r'^steel/$',views.steel, name='steel'),
	url(r'^(?P<jewelry_type>[A-Za-z0-9]+)/(?P<jewelry_style_user>[A-Za-z0-9]+)/$',views.style,name="style"),
	url(r'^(?P<jewelry_type>[A-Za-z0-9]+)/(?P<jewelry_style_user>[A-Za-z0-9]+)/(?P<jewelry_id>[0-9]+)/$',views.style_specific,name="style_specific"),	
]
