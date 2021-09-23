from django.urls import path
from .views import *
from dynamic_rest.routers import DynamicRouter

urlpatterns = [
    # path('', ProductsAPI.as_view(), name='All_products'),
    # path('<int:id>', ProductItem.as_view(), name='specefic_products'),
    # path('category/<slug:category>', CategoryAPI.as_view(), name='Men_products'),
    path('products/<slug:slug>/', ProductItemAPI.as_view(), name='product_detail'),
    path('categories/<slug:slug>/', CategoryAPI.as_view(), name='category_detail'),
    path('cart/<slug:slug>/', CartAPI.as_view(), name='cart_detail'),
]
router = DynamicRouter()

router.register(r'products', AllProduct)
router.register(r'categories', AllCategories)
router.register(r'colors', AllProductColors)
# router.register(r'cart', Cart)

app_name = "product"
urlpatterns += router.urls
