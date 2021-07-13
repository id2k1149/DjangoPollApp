from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=32, unique=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    created = models.DateField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Menu'


class User(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Result(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField()


