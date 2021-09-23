from django.urls import path, include
from .views import *

urlpatterns = [
    path('sign_up/', User_creation.as_view(), name='sign_up'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('home/', include('home.urls')),
]