import jewelry.models as jewelry_models
import inspect

#given a selected class jewelry_type, parses out the appropriate Django Model
#NOTE: see context_processors.py for the alternate version
def class_parser(jewelry_type):
	for name,obj in inspect.getmembers(jewelry_models):
		if inspect.isclass(obj) and obj.__name__ == jewelry_type:
			return obj
	return None

def getParameters(classname):
	obj = class_parser(classname)
	parameters = []
	for param in obj._meta.get_fields():
		if param.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField','DateTimeField']:
			parameters.append(param.name)
	return parameters


