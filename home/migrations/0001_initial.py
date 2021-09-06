# Generated by Django 3.2.6 on 2021-08-16 21:46

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ground_image', models.ImageField(blank=True, null=True, upload_to=home.models.get_home_image_path)),
                ('text_one', models.TextField(blank=True, max_length=255, null=True)),
                ('video', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]