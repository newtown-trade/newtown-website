from django.db import models

class Metal(models.Model):
	GOLD = 'Gold'
	SILVER = 'Silver'
	BRONZE = 'Bronze'
	STEEL = 'Steel'
	
	METAL_CHOICES = (
		(GOLD,'Gold'),
		(SILVER,'Silver'),
		(BRONZE,'Bronze'),
		(STEEL,'Steel'),	
	)	
	jewelry_type = models.CharField(max_length=50)
	size = models.IntegerField(default=0)#change to float later if necessary
	metal = models.CharField(max_length=50, choices=METAL_CHOICES,default=GOLD)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	#to add image later

	def __str__(self):
		output = self.metal + ' ' + self.jewelry_type + ', ' + str(self.size) + ' mm.'
		return output
