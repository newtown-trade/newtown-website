#additional settings for Algolia's Indexing of the Jewelry class
#this is where facets (i.e. search refinement options are declared)
#attributesForFaceting should ALWAYS be model fields ONLY (this should be automated)

from algoliasearch_django import AlgoliaIndex

class MetalIndex(AlgoliaIndex):
	settings={'attributesForFaceting':['metal','jewelry_type','price','size']}
class ContactLenseIndex(AlgoliaIndex):
	settings={'attributesForFaceting':['color','size','price']}
