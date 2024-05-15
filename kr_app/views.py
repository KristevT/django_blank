from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
 

class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
