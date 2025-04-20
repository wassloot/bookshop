from django.shortcuts import render, redirect
from .models import Tea
from .forms import TeaForm
from django.shortcuts import get_object_or_404, redirect
from .cart import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse

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

