#additional settings for Algolia's Indexing of the Jewelry class
#this is where facets (i.e. search refinement options are declared)
#attributesForFaceting should ALWAYS be model fields ONLY (this should be automated)

from algoliasearch_django import AlgoliaIndex

class MetalIndex(AlgoliaIndex):
	parameters = ['jewelry_type','price','size','jewelry_style']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
class ContactLenseIndex(AlgoliaIndex):
	parameters = ['size','price','jewelry_style']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
class DisplayIndex(AlgoliaIndex):
	parameters = ['name','full_price','length','width']
	settings = {'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
