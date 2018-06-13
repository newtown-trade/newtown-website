from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from .index import * 

class JewelryConfig(AppConfig):
	name = 'jewelry'

	#registers  models with django and algolai
	def ready(self):
		Metal = self.get_model('Metal')
		algoliasearch.register(Metal,MetalIndex)
		ContactLense = self.get_model('ContactLense')
		algoliasearch.register(ContactLense,ContactLenseIndex)
		Display = self.get_model('Display')
		algoliasearch.register(Display,DisplayIndex)
