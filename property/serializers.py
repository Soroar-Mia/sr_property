from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PropertySerializer(serializers.ModelSerializer):
    purpose = serializers.StringRelatedField(many=True)
    property_type = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Property
        fields = '__all__'
        
class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purpose
        fields = '__all__'
        
class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PropertyType
        fields = '__all__'
        

        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'




class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.save()
        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)