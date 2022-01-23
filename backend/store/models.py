from django.db import models
from django.conf import settings

from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.TextField()
    hash = models.CharField(max_length=15)
    user_transaction_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


#automtically generates a token 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)