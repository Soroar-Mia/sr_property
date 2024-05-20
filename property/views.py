from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


class PurposeViewset(viewsets.ModelViewSet):
    queryset = models.Purpose.objects.all()
    serializer_class = serializers.PurposeSerializer
    
    
class PropertyTypeViewset(viewsets.ModelViewSet):
    queryset = models.PropertyType.objects.all()
    serializer_class = serializers.PropertyTypeSerializer
    

class PropertyPagination(pagination.PageNumberPagination):
    page_size = 3 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class PropertyViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = PropertyPagination
    search_fields = ['location', 'purpose__name', 'property_name', 'city', 'property_type__name']
    
class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    


class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response("Form Done")
        return Response(serializer.errors)
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        return Response(serializer.errors, status=400)
    
    
class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')
