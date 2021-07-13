from django.urls import path
from polls_app import views

app_name = 'polls_app'


urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_restaurant, name='add'),
    path('menu/<int:filter_id>', views.menu, name='menu'),

]
