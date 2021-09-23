from dynamic_rest.fields import DynamicMethodField, DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from .models import *
from rest_framework import serializers


class ProductReviewSerializer(DynamicModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(DynamicModelSerializer):
#     category_data = DynamicMethodField(read_only=True)

    # colors = ProductColorSerializer(read_only=True, embed=True, many=True, source='product_color')
#
#     categoryyyyyyy = CategorySerializer(read_only=True, embed=True,
#         source='category')
#
#     def get_category_data(self, obj):
#         return CategorySerializer(obj.category).data
    reviews = ProductReviewSerializer(read_only=True, embed=True, many=True, source='review_product')

    class Meta:
        model = Product
        # depth = 1
        fields = '__all__'


class CategorySerializer(DynamicModelSerializer):
    # products = DynamicRelationField(
    #     ProductSerializer, embed=True, read_only=True, many=True,
    #     source='category_product'
    # )

    products = ProductSerializer(read_only=True, embed=True, many=True, source='category_product')

    class Meta:
        model = Category
        fields = '__all__'


class ProductColorSerializer(DynamicModelSerializer):
    # product = ProductSerializer(embed=True, read_only=True)
    category_data = DynamicMethodField(read_only=True)

    def get_category_data(self, obj):
        category = Category.objects.filter(category_product__product_color__name=obj.name)
        return CategorySerializer(category, many=True).data

    class Meta:
        model = ProductColor
        fields = '__all__'

class CartItemSerializer(DynamicModelSerializer):
    product = ProductSerializer(embed=True, read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(DynamicModelSerializer):

    cart_item = CartItemSerializer(embed=True, many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'










