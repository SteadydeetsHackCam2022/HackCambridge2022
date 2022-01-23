from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render

from django.http import Http404
from .models import Product
from .forms import ProductForm
from .phash import Phash
import io
import cv2
import numpy as np

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
    src_img = ""
    products = Product.objects.all()
    scores = Phash.phash_list(src_img, products)
    # get second element from each tuple and save in dict
    scores_dict = {product.id: score for product, score in scores}
    return render(request, 'feed.html', context = scores_dict )

def profile(request):
    return render(request, 'profile.html')

def product_add(request):
    return render(request, 'add_product.html')

def product_save(request):
    if request.method != 'POST':
        return

    form = ProductForm(request.POST, request.FILES)

    # get image from django form
    image = request.FILES['image']
    # download image form request
    image_file = io.BytesIO(image.read())
    # open image_file image
    img = cv2.imdecode(np.fromstring(image_file.getvalue(), np.uint8), cv2.IMREAD_UNCHANGED)


    hash = Phash.get_phash(img)
    # save hash to form
    form.instance.hash = hash
    if form.is_valid():
        form.save()
    else:
        print("form is not valid")
    return render(request, 'add_product.html')
