from django.shortcuts import render


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ProductSerializer
from .models import Product

class GetProduct(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, pk):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
