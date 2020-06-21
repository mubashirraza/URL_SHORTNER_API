from django.db import models

# Create your models here.
class ShortUrl(models.Model):
	short_url = models.CharField(max_length=20)
	long_url = models.URLField(max_length=200)

	def __str__(self):
		return f"{self.long_url} => {self.short_url}"