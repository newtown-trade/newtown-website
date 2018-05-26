#additional settings for Algolia's Indexing of the Jewelry class
#this is where facets (i.e. search refinement options are declared)

from algoliasearch_django import AlgoliaIndex

class MetalIndex(AlgoliaIndex):
	settings={'attributesForFaceting':['metal','jewelry_type']}
