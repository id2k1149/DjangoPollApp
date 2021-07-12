from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Dish(models.Model):
    name = models.CharField(max_length=32, unique=True)
    price = models.PositiveIntegerField()
