from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from shop import views as shop_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_views.tea_list, name='tea_list'),
    path('register/', shop_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tea_list'), name='logout'),
    path('', views.tea_list, name='tea_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:tea_id>/', views.cart_add, name='cart_add'),
    path('checkout/', views.checkout, name='checkout'),
    path('add/', views.add_tea, name='add_tea'),
    path('payment-method/', shop_views.payment_method_view, name='payment_method'),
    path('', shop_views.tea_list, name='tea_list'),
    path('cart/', shop_views.cart_view, name='cart_view'),
    path('cart/add/<int:tea_id>/', shop_views.cart_add, name='cart_add'),
    path('checkout/', shop_views.checkout, name='checkout'),
    path('register/', shop_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tea_list'), name='logout'),
    path('link-card/', shop_views.link_card, name='link_card'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('logout/', LogoutView.as_view(next_page='tea_list'), name='logout'),
]

