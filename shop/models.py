from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    origin = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)  # MM/YY
    cvv = models.CharField(max_length=3)