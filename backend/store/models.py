from django.db import models

# Create your models here.

SIZE_CHOICES = [
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL')
]

GENDER_CHOICES = [
    ('m', 'Male'),
    ('f', 'Female'),
    ('u', 'Unisex')
]

class Product(models.Model):
    colour = models.CharField(max_length=15)
    brand = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_place=2)
    condition = models.TextField()