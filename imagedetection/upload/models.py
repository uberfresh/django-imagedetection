from django.db import models
from django.urls import reverse



# Create your models here.


class Upload(models.Model):
	image = models.ImageField()
	detected_image = models.ImageField(blank=True,null = True)
	det_objects = models.CharField(max_length=250,blank=True,null=True)
	det_probabilty = models.CharField(max_length = 250,blank=True,null=True)


     
	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('upload:detectedimage',kwargs={'pk':self.pk})
