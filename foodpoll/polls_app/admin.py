from django.contrib import admin
from .models import User, Restaurant, Result, Vote, Dish, Menu

# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Result)
admin.site.register(Vote)
admin.site.register(Dish)
admin.site.register(Menu)
