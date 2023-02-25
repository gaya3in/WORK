from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, filters
from .serializers import LoginSerializer, RegisterSerializer, WorkSerializer
from django.contrib.auth import login,logout
from .models import Work,Client,Artist
from django_filters.rest_framework import DjangoFilterBackend
import json

# Create your views here.

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        try:
            # data = json.loads(request.body.decode('utf-8'))
            serializer = self.serializer_class(data=request.data,
                context={ 'request': self.request })
            serializer.is_valid(raise_exception=False)
            if serializer.errors:
                return Response("Access denied: wrong username or password",status=status.HTTP_401_UNAUTHORIZED)
            else:
                user = serializer.validated_data['user']
                login(request, user)
                data = {"message": "User Authenticated."}
                return Response(data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response("Exception Occured!!!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.errors:
                return Response("Access denied: wrong username or password",status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save()
                data = {"message": "User Registration Successful."}
                return Response(data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response("Exception Occured!!!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


class ListWork(ModelViewSet):    
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type']
    search_fields = ['artist__name']
    
    def get_queryset(self):
        works = Work.objects.all()
        return(works)
        
