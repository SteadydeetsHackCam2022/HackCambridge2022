from django.db import models
from django.conf import settings

from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.FileField(upload_to='pictures_carbonclothes')
    hash = models.TextField(max_length=32)


#automtically generates a token 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)