from django.shortcuts import render, redirect
from .models import MenuItem, SliderItem
from .forms import CustomerForm

# Create your views here.

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})

def slider_view(request):
    items = SliderItem.objects.all()
    return render(request, 'menu/index.html', {'items': items})

def customer_form_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerForm()

    return render(request, 'menu/customer_form.html', {'form': form})

def success_view(request):
    return render(request, 'menu/success.html')

def about(request):
    return render(request, 'menu/about.html')