from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render

from django.http import Http404
from .models import Product
from .forms import ProductForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        if form.confirm_login_allowed():
            return render(request, 'login.html', context={
                'created': True
            })

        return render(request, 'login.html')
    elif request.method == 'GET':  
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'signup.html', context={
                'created': True
            })

    return render(request, 'signup.html', )

def feed(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'feed.html', context=context)

def search(request):
    return render(request, 'search.html')

def profile(request):
    return render(request, 'profile.html')

def product_add(request):
    return render(request, 'add_product.html')

def product_save(request):
    if request.method != 'POST':
        return
    
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
