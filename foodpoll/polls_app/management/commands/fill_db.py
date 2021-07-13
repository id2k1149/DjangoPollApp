from django.core.management.base import BaseCommand
from polls_app.models import Restaurant, Menu


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("fill_db")
        restaurants = Restaurant.objects.all()
        for each in restaurants:
            print(each.name, each.id)
            menu = Menu.objects.filter(restaurant_id=each.id)
            for item in menu:
                print(item.dish_id)




