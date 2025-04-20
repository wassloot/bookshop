from django.urls import path
from . import views

urlpatterns = [
    path('', views.tea_list, name='tea_list'),
<<<<<<< HEAD
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:tea_id>/', views.cart_add, name='cart_add'),
    path('checkout/', views.checkout, name='checkout'),
]
=======
    path('add/', views.add_tea, name='add_tea'),
]
>>>>>>> 186fde388756c4ffb247f62bf01be81247781ab2
