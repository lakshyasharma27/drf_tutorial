from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.db import IntegrityError
from user.serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from utils import custom_exceptions
from rest_framework.views import APIView

# Create your views here.
class RegisterUser(APIView):
    permission_classes = []
    
    def post(self, request, format=None):
        data = request.data
        serializer = RegisterUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except IntegrityError as ie:
            raise custom_exceptions.UniqueConstraintException(ie)
        return Response("User successfully created.", status=status.HTTP_201_CREATED)
    
class LoginUser(APIView):
    permission_classes = []
    
    def post(self, request, format=None):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
