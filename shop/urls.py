from django.urls import path
from . import views

urlpatterns = [
    path('', views.tea_list, name='tea_list'),
    path('add/', views.add_tea, name='add_tea'),
]