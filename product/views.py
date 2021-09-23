from django.db.models import Sum
from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .models import Product
from django.shortcuts import get_object_or_404
from .models import *
from dynamic_rest.viewsets import DynamicModelViewSet

# class ProductsAPI(APIView):
#
#     permission_classes = ()
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True).data
#         return Response({"Data": serializer}, status=status.HTTP_200_OK)


class AllProduct(DynamicModelViewSet):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, queryset=None):
        category = self.request.query_params.get('category', None)
        if category:
            return self.queryset.filter(category__slug=category)
        return self.queryset


class AllCategories(DynamicModelViewSet):
    permission_classes = ()
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self, queryset=None):
        category = self.request.query_params.get('category', None)
        if category:
            return self.queryset.filter(slug=category)
        return self.queryset


class AllProductColors(DynamicModelViewSet):
    permission_classes = ()
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class ProductItemAPI(APIView):

    permission_classes = ()

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product).data
        # print(serializer.id)
        return Response({"Data": serializer}, status=status.HTTP_200_OK)


class CategoryAPI(APIView):
    permission_classes = ()

    def get(self, request, slug):
        print(slug)
        products = Product.objects.filter(category__slug=slug)
        serializer = ProductSerializer(products, many=True).data
        return Response({slug: serializer}, status=status.HTTP_200_OK)


class CartAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        total_price = 0
        user = request.user
        cart = Cart.objects.filter(user=user)
        serializer = CartSerializer(cart.first()).data
        # for cart_item in cart_items:
        #     total = cart_items.product.price * cart_item.quantity
        if cart:
            cart = cart.first()
        #     cart = cart.first()
        #     serializer = CartSerializer(cart).data
        #     total_price = cart.product.all().aggregate(total_price=Sum('price')).get('total_price', 0)
        #     cart.total_price = total_price
        #     cart.save()
            cart_items = cart.cart_item.all()
            for cart_item in cart_items:
                total_price += cart_item.quantity * cart_item.product.price

            cart.total_price = total_price
            cart.save()
            return Response({'Data': serializer}, status=status.HTTP_200_OK)
        return Response({'Data', "Not cart found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug):
        error = []
        cart_item = CartItem.objects.filter(product__slug=slug, cart__user=request.user).first()
        if cart_item:
            cart_item.delete()
            return Response({"Data", "Done"}, status=status.HTTP_200_OK)
        error.append(f"This {slug} is not found ")
        return Response({"Data", error}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, slug):
        quantity = request.data.get("quantity", None)

        if quantity and isinstance(quantity, int):
            cart_item = CartItem.objects.filter(product__slug=slug, cart__user=request.user).first()
            # product_item = ProductItem.objects.filter(sku=slug).first()
            product_item = ProductItem.objects.filter(sku=slug).first()
            print(product_item)

            if cart_item and product_item.quantity >= quantity:
                cart_item.quantity += quantity
                cart_item.cart.total_price += cart_item.product.price * quantity
                cart_item.save()
                cart_item.cart.save()
                serializer = CartSerializer(cart_item.cart).data
                return Response({'Data': serializer}, status=status.HTTP_200_OK)
        return Response({'Data': "Out Of Stock"}, status=status.HTTP_400_BAD_REQUEST)





