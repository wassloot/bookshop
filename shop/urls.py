from django.urls import path
from . import views

urlpatterns = [
    path('', views.tea_list, name='tea_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:tea_id>/', views.cart_add, name='cart_add'),
    path('checkout/', views.checkout, name='checkout'),
]
