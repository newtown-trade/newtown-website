#additional settings for Algolia's Indexing of the Jewelry class
#this is where facets (i.e. search refinement options are declared)
#attributesForFaceting should ALWAYS be model fields ONLY (this should be automated)

from algoliasearch_django import AlgoliaIndex

class MetalIndex(AlgoliaIndex):
	parameters = ['metal','jewelry_type','price','size']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}
class ContactLenseIndex(AlgoliaIndex):
	parameters = ['color','size','price']
	settings={'attributesForFaceting':parameters,'searchableAttributes':parameters,'attributesToHighlight':parameters}

