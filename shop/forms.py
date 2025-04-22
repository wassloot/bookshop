from .models import Tea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PaymentMethod

class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = ['name', 'description', 'price', 'origin', 'in_stock']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['card_number', 'expiration_date', 'cvv']