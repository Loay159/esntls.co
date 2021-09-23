from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Review(models.Model):
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True, default=5)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.user.username} {self.product.name} {self.title}'
