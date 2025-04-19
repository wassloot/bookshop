from django.contrib import admin
from django.urls import path, include
from shop.views import tea_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tea_list, name='tea_list'),
    path('', include('shop.urls')),
]