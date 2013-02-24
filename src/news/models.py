from django.db import models

# Create your models here.
class Channel(models.Model):
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.url