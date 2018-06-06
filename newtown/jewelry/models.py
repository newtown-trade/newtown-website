from django.db import models

#additional classes/fields will be implemented depending on production needs

#returns dynamic folder structure for Metal
#this produces a SuspiciousFileOperation that Django rejects
def upload_metal(instance,filename):
	return 'metals/%s/%s/%s' % (instance.metal, instance.jewelry_type.replace(" ","_"),filename)

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
	jewelry_type = models.CharField(max_length=50,verbose_name="Type of Jewelry")
	size = models.IntegerField(default=0,verbose_name="Size (mm.)")#change to float later if necessary, expressed in millimetres
	metal = models.CharField(max_length=50, choices=METAL_CHOICES,default=GOLD,verbose_name="Type of Metals")
	price = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Price")
	image = models.ImageField(upload_to=upload_metal,null=True)

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
	name=models.CharField(max_length=50,default="name")
	jewelryset = models.ManyToManyField(Metal,verbose_name="Jewelry in Display")
	full_price = models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Price of Entire Display")
	length=models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Length of Board (mm.)")
	width=models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name="Width of Board (mm.)")

#class for Contact Lenses
#separated because totally different stats
class ContactLense(models.Model):
	color=models.CharField(max_length=50)
	size=models.IntegerField(default=0)
	price=models.DecimalField(max_digits=6,decimal_places=2)
