from product.models import Category
from product.models import Product
from .models import HomePage
from rest_framework import serializers
from product.serializer import *


class HomePageSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('get_categories')
    products = serializers.SerializerMethodField('get_products')

    def get_categories(self, obj):
        categories = Category.objects.filter(is_home=True, is_archive=False)
        return CategorySerializer(categories, many=True).data

    def get_products(self, obj):
        products = Product.objects.filter(is_home=True, is_archive=False)
        return ProductSerializer(products, many=True).data


    class Meta:
        model = HomePage
        fields = ('ground_image', 'video', 'text_one', 'categories', 'products')
