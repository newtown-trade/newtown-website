import jewelry.models as jewelry_models
import inspect

def navbar_generate(request):

	#ieterates through all classes in models.py, and checks if it's a valid class
	#for each valid class, adds another entry to the Python dictionary 'jewelry_classes' as so:
	#'display name of jewelry':[array of entered styles,internal name of object, object itself]
	jewelry_classes={}
	for name,obj in inspect.getmembers(jewelry_models):
		if inspect.isclass(obj) and obj.__name__ not in ['Display','Side']:
			jewelry_classes[obj._meta.verbose_name]=[obj.objects.values_list('jewelry_style',flat=True),obj.__name__,obj]
	
	#returns additional dict to be contributed
	return {'jewelry_classes':jewelry_classes}

