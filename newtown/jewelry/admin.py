from django.contrib import admin
from .models import *
class DisplayAdmin(admin.ModelAdmin):
	filter_horizontal=('jewelryset',)
admin.site.register(Metal)
admin.site.register(Display,DisplayAdmin)
admin.site.register(ContactLense)
admin.site.site_header="Newtown Trade Site Administration"

#testing suite for TestModels
class TestAInLine(admin.StackedInline):
	model=TestA
	classes=['collapse']
class TestBInLine(admin.StackedInline):
	model=TestB
	classes=['collapse']

class MasterTestAdmin(admin.ModelAdmin):
	inlines=[TestAInLine,TestBInLine]

admin.site.register(TestA)
admin.site.register(MasterTest,MasterTestAdmin)
# Register your models here.
