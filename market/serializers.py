from rest_framework import serializers
from market.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'in_stock', 'category']


class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['in_stock']
