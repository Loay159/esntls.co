from django.db import models
import os
from django.utils.text import slugify
from django.contrib.auth.models import User

def get_product_image_path(instance, filename):
    return os.path.join('product', 'img', filename)


class Category(models.Model):
    photo = models.ImageField(upload_to=get_product_image_path, null=True, blank=True)
    name = models.CharField(max_length=255)
    is_home = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name="category_product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    is_home = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class ProductColor(models.Model):
    COLOR_CHOICES = (
        ("red", "Red"),
        ("blue", "Blue"),
        ("yellow", "Yellow"),
        ("white", "White"),
        ("black", "Black"),
        ("green", "Green"),
    )
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="red")
    product = models.ForeignKey(Product, related_name="product_color", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.color


class Size(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey(ProductColor, related_name="color_size", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    sku = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    size = models.ForeignKey(Size, related_name="size_item", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.sku


class ProductImages(models.Model):
    image = models.ImageField(upload_to=get_product_image_path, null=True, blank=True)
    color = models.ForeignKey(ProductColor, related_name="color_image", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review_product')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    stars_count = models.IntegerField(default=5)
    comment = models.TextField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    total_price = models.IntegerField(default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart_item')
    quantity = models.IntegerField(default=1)



