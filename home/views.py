from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .models import *
from .serializer import HomePageSerializer
from rest_framework.exceptions import NotAcceptable


class HomePageAPI(APIView):

    permission_classes = ()

    def get(self, request):
        queryset = HomePage.objects.first()
        if queryset:
            serializer = HomePageSerializer(queryset)
            return Response({"Data": serializer.data}, status=status.HTTP_200_OK)
        raise NotAcceptable('Not Found')






