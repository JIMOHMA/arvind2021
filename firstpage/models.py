from django.db import models

# Create your models here.
class Product(models.Model):
	# variable attributes for the class Product
	id 			= models.BigAutoField(primary_key=True)
	title 		= models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places = 2, max_digits=1000)
	image 		= models.ImageField(null=True, blank=True)
	listing_id	= models.IntegerField(blank=True, null=True)
	productLink = models.URLField(max_length=200)

	# method attribute for the class Product
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url