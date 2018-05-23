from django.apps import AppConfig
import algoliasearch_django as algoliasearch

class JewelryConfig(AppConfig):
	name = 'jewelry'

	#registers Metal model with django
	def ready(self):
		Metal = self.get_model('Metal')
		algoliasearch.register(Metal)
