from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=40)
	position = models.IntegerField()
	stars = models.IntegerField()
	address = models.CharField(max_length=100)
	country = models.CharField(max_length=20)
	coordinates = models.CharField(max_length=40)
	phone_no = models.IntegerField()
	email = models.CharField(max_length=30)
	website = models.CharField(max_length=30)




