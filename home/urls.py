from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageAPI.as_view(), name='home_page'),
]