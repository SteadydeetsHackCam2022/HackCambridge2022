from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['colour', 'brand', 'type', 'size', 'gender', 'price', 'condition', 'hash', 'user_transaction_id']