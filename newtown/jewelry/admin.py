from django.contrib import admin
from .models import *
class DisplayAdmin(admin.ModelAdmin):
	filter_horizontal=('jewelryset',)
admin.site.register(Metal)
admin.site.register(Display,DisplayAdmin)
admin.site.register(ContactLense)
# Register your models here.
