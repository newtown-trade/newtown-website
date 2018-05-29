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
	size = models.IntegerField(default=0)#change to float later if necessary, expressed in millimetres
	metal = models.CharField(max_length=50, choices=METAL_CHOICES,default=GOLD)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	#to add image later

	def __str__(self):
		output = self.metal + ' ' + self.jewelry_type + ', ' + str(self.size) + ' mm.'
		return output
	
	#standardizes future submissions of jewelry types by automatically capitalizing them
	#goal: decrease busywork by not requiring tuple for jewelry type, for optimal flexibility
	def save(self, *args, **kwargs):
		self.jewelry_type = self.jewelry_type.title()
		super(Metal,self).save(*args,**kwargs)

#class for jewelry display
#need: length, width, total 
class Display(models.Model):
	jewelryset = models.ManyToManyField(Metal,verbose_name="Jewelry in Display")
	full_price = models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Price of Entire Display")
	length=models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Length of Board")
	width=models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Width of Board")
