from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(ModelSerializer):
    is_fine = serializers.SerializerMethodField()

    def get_fineness(self, obj):
        return obj.is_fine

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    max_price = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()

    def get_max_price(self, obj):
        return obj.max_price
    
    def get_min_price(self, obj):
        return obj.min_price
    
    class Meta:
        model = Category
        fields = '__all__'