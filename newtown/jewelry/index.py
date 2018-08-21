#additional settings for Algolia's Indexing of the Jewelry class
#this is where facets (i.e. search refinement options are declared)
#attributesForFaceting should ALWAYS be model fields ONLY (this should be automated)

from algoliasearch_django import AlgoliaIndex

'''
from class_parser import *

def get_parameters(classname):
	obj = class_parser(classname)
	parameters = []
	for param in obj._meta.get_fields():
		if param.get_internal_type() not in ['ManyToManyField','AutoField','FileField','ImageField','DateTimeField']:
			parameters.append(param)
	return param

print(get_parameters('Metal'))
'''

class MetalIndex(AlgoliaIndex):
	parameters = ['jewelry_type','price','size','jewelry_style']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
class ContactLenseIndex(AlgoliaIndex):
	parameters = ['size','price','jewelry_style']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
class DisplayIndex(AlgoliaIndex):
	parameters = ['name','full_price','length','width']
	settings = {'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
