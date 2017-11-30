from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	email = models.EmailField()

	def __str__(self):
		return self.name + " @ " + self.email
