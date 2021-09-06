from django.db import models
import os


def get_product_image_path(instance, filename):
    return os.path.join('product', 'img', filename)

class Category(models.Model):
    photo = models.ImageField(upload_to=get_product_image_path, null=True, blank=True)
    name = models.CharField(max_length=255)
    is_home = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category,related_name="product_category", on_delete=models.CASCADE)

class ProductColor(models.Model):
    COLOR_CHOICES = (
        ("red","Red"),
        ("blue", "Blue"),
        ("yellow", "Yellow"),
        ("white", "White"),
        ("black", "Black"),
        ("green", "Green"),
    )
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="Red")


class Size(models.Model):
    name = models.CharField(max_length=20)
    color_size = models.ManyToManyField(ProductColor, related_name="color_size")


class ProductItem(models.Model):
    sku = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    product_size = models.ManyToManyField(Size, related_name="product_size")



