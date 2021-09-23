from django.db import models
import os


def get_home_image_path(instance, filename):
    return os.path.join('home', 'img', filename)


class HomePage(models.Model):
    ground_image = models.ImageField(upload_to=get_home_image_path, blank=True, null=True)
    text_one = models.TextField(max_length=255, blank=True, null=True)
    video = models.FileField(null=True, blank=True)




