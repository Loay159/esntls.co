from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
# from .models import User
from rest_framework import status
from django.contrib.auth.models import Permission, User
from django.core.mail import send_mail
from django.conf import settings


error =[]


class User_creation(APIView):

    permission_classes = [IsAuthenticated]

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.action = None

    def post(self,request):
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        password = request.data.get("password", None)
        email = request.data.get("email", None)

        if not first_name:
            error.append(f"first name is required")

        if not last_name:
            error.append(f"last name is required")

        if not password:
            error.append(f"password is required")

        if not email:
            error.append(f"email is required")

        user = User.objects.filter(username=email).values()
        if user:
            error.append(f"The username is already exists")
            return Response({"error":error})
        user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password, username=email, email=email)
        return Response({"The user is created"}, status.HTTP_201_CREATED)

    # # Get all users
    # def get(self,request):
    #     users = User.objects.all().values()
    #     return Response (users)
    # def get_permissions(self):
    #     if self.action == 'put':
    #         return [IsAuthenticated()]
    #update a specefic user
    # @action(detail=False, permission_classes=[IsAuthenticated])
    def put(self, request):
        new_first_name = request.data.get("first_name", None)
        new_last_name = request.data.get("last_name", None)
        new_email = request.data.get("email", None)
        print(request.data)
        # user = User.objects.filter(username=username)
        user = request.user
        print(user)
        if user:
            # user = user.first()
            # user.first_name = new_first_name
            # user.last_name = new_last_name
            # user.email = new_email
            # user.save()
            return Response({"user data is updated"})
        return Response({"user is not found"})


class ResetPassword(APIView):

    permission_classes = ()

    def post(self, request):
        email = request.data.get("email", None)
        print(email)

        if not email:
            return Response({f"{email} is not found" })

        subject = "Greetings from Loay"
        msg = "Please reset your account password"
        to = email
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        if (res == 1):
            msg = "Mail Sent Successfully."
        else:
            msg = "Mail Sending Failed."
        return Response(msg)












