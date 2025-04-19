from django.shortcuts import render, redirect
from .models import Tea
from .forms import TeaForm

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