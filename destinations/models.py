from django.db import models

# Create your models here.
class Destination(models.Model):
	name = models.TextField()
	address = models.TextField()
	region = models.TextField()

	def __str__(self):
		return '%s %s %s' % (self.name, self.address, self.region)