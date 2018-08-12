import jewelry.models as jewelry_models
import inspect

#given a selected class jewelry_type, parses out the appropriate Django Model
#NOTE: see context_processors.py for the alternate version
def class_parser(jewelry_type):
	for name,obj in inspect.getmembers(jewelry_models):
		if inspect.isclass(obj) and obj.__name__ == jewelry_type:
			return obj
	return None
