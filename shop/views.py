from django.shortcuts import render, redirect
from .models import Tea
from .forms import TeaForm
from django.shortcuts import get_object_or_404, redirect
from .cart import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from .forms import RegisterForm
from .forms import PaymentForm
from .models import PaymentMethod
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import redirect

def tea_list(request):
    teas = Tea.objects.all()
    return render(request, 'shop/tea_list.html', {'teas': teas})

def add_tea(request):
    if request.method == 'POST':
        form = TeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tea_list')
    else:
        form = TeaForm()

    return render(request, 'shop/add_tea.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect


def cart_add(request, tea_id):
    cart = Cart(request)
    tea = get_object_or_404(Tea, id=tea_id)
    cart.add(tea=tea)

    # Перенаправляем обратно на страницу списка чая
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('tea_list')))


def cart_view(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

def checkout(request):
    cart = Cart(request)
    # Тут ты можешь потом подключить оплату
    return render(request, 'shop/checkout.html', {'cart': cart})

    return render(request, 'shop/add_tea.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tea_list')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})

@login_required
def payment_method_view(request):
    try:
        payment = request.user.paymentmethod
    except PaymentMethod.DoesNotExist:
        payment = None

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            method = form.save(commit=False)
            method.user = request.user
            method.save()
            return redirect('tea_list')
    else:
        form = PaymentForm(instance=payment)

    return render(request, 'shop/payment_method.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tea_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def link_card(request):
    return render(request, 'shop/link_card.html')

def cart_clear(request):
    request.session['cart'] = {}
    return redirect('cart_view')