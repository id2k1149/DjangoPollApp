from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu


# Create your views here.
def main_view(request):
    restaurants = Restaurant.objects.all()
    menu = Menu.objects.all()
    return render(request, 'polls_app/index.html', context={'restaurants': restaurants, 'menu': menu})


def create_restaurant(request):
    return render(request, 'polls_app/create.html')


def menu(request, filter_id):
    menu = Menu.objects.filter(restaurant_id=filter_id)
    return render(request, 'polls_app/menu.html', context={'menu': menu})
