from django.db import models

class Jewelry(models.Model):
	jewelry_type = models.CharField(max_length=50)
	size = models.IntegerField(default=0)
	metal = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	#to add image later

	def __str__(self):
		output = self.metal + ' ' + self.jewelry_type + ', ' + str(self.metal)
