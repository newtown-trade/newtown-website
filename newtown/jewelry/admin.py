from django.contrib import admin
from .models import *
class DisplayAdmin(admin.ModelAdmin):
	filter_horizontal=('metal_set','contactLense_set',)
admin.site.register(Metal)
admin.site.register(Display,DisplayAdmin)
admin.site.register(ContactLense)
admin.site.site_header="Newtown Trade Site Administration"
# Register your models here.
