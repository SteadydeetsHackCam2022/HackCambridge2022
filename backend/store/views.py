from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from . models import *
from rest_framework.response import Response
from . serializer import *

# Create your views here.
def add_product(request):
    product_data = JSONParser().parse(request)
    serializer = ProductSerializer(data=product_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

def delete_product(request, key):
    try:
        product = Product.objects.get(pk=key)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return JsonResponse({'message': 'Product deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)