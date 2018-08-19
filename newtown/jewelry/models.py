from django.db import models
from django.utils import timezone

'''
additional classes/fields will be implemented depending on production needs

CLASS STUCTURE TO FOLLOW:

class JewelryType(models.Model):
	
	jewelry_style = [MODEL TO APPEAR ON NAVBAR]
	price = [PRICE FIELD FOR MODEL]
	image = [IMAGE FIELD FOR MODEL]

	everything else
'''

#returns dynamic image folder structure for Metal
def upload_metal(instance,filename):
	return 'metals/%s/%s/%s' % (instance.metal, instance.jewelry_type.replace(" ","_"),filename)
#dynamic folder image folder structure for ContactLEnse
def upload_lense(instance,filename):
	return 'contactLense/%s/%s' % (instance.color,filename)

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
	jewelry_style = models.CharField(max_length=50, choices=METAL_CHOICES,default=GOLD,verbose_name="Type of Metals")
	price = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Price")
	image = models.ImageField(upload_to=upload_metal,null=True)
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		output = self.jewelry_style + ' ' + self.jewelry_type + ', ' + str(self.size) + ' mm.'
		return output
	
	#standardizes future submissions of jewelry types by automatically capitalizing them
	#goal: decrease busywork by not requiring tuple for jewelry type, for optimal flexibility
	def save(self, *args, **kwargs):
		self.jewelry_type = self.jewelry_type.title()
		super(Metal,self).save(*args,**kwargs)

	class Meta:
		verbose_name='Earring, Nose Hook, Bracelet' #this will need to expand later		
		verbose_name_plural= 'Earrings, Nose Hooks, Bracelets'

#class for Contact Lenses
#separated because totally different stats
class ContactLense(models.Model):
	COLORS = (
		('Purple','Purple'),
		('Blue','Blue'),
		('Green','Green'),
		('Yellow','Yellow'),
		('Orange','Orange'),
		('Red','Red'),
	)	
	jewelry_style=models.CharField(max_length=50,choices=COLORS,default='Red',verbose_name='Color')
	size=models.IntegerField(default=0,verbose_name='Size (mm.)')
	price=models.DecimalField(max_digits=6,decimal_places=2,verbose_name='Price')
	image = models.ImageField(upload_to=upload_lense,null=True)
	timestamp=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.jewelry_style + ' Lense, ' + str(self.size) + ' mm.'

	class Meta:
		verbose_name='Contact Lense'
		verbose_name_plural='Contact Lenses'

#class for jewelry display
#need: length, width, total 
class Display(models.Model):
	name=models.CharField(max_length=50,default="name",verbose_name="Name of Display")

	#ADD A MANYTOMANYFIELD FOR EACH NEW JEWELRY MODEL, follow convention "{{metalCase}}_set"
	#also be sure to add the ManyToManyField to the filter_horizontal option in admin.py
	metal_set = models.ManyToManyField(Metal,verbose_name=Metal._meta.verbose_name_plural + " In Display",blank=True)
	contactLense_set = models.ManyToManyField(ContactLense,verbose_name=ContactLense._meta.verbose_name_plural + " In Display",blank=True)

	full_price = models.DecimalField(decimal_places=2,max_digits=6,default=0,verbose_name="Price of Entire Display")
	length=models.IntegerField(default=0,verbose_name="Length of Board (mm.)")
	width=models.IntegerField(default=0,verbose_name="Width of Board (mm.)")
	image = models.ImageField(upload_to='display/', null=True, verbose_name = "Image of Display") #TODO: create specialized folders for display after input from dad
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name + ', ' + str(self.length) + ' mm. X ' + str(self.width) + ' mm., $' + str(self.full_price)
	class Meta:
		verbose_name='Display'
		verbose_name_plural="Displays"

