from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu_categories/', views.menu_categories, name='menu_categories'),
    path('single_categories/', views.single_categories, name='single_categories'),

]