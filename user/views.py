from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from user.send_mail import send_confirmation_email
from . import serializers
from .serializers import ActivationSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = serializers.RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Success', status=status.HTTP_201_CREATED)
        return Response('Error', status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def post(self, request, activation_code):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Success', status=status.HTTP_200_OK)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer

