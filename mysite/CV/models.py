from django.db import models

class Section(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.title
