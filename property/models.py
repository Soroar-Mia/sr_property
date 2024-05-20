from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Purpose(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
class PropertyType(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
            return self.name

class Property(models.Model):
    location = models.CharField(max_length = 40)
    slug = models.SlugField(max_length = 50)
    purpose = models.ManyToManyField(Purpose)
    property_type =  models.ManyToManyField(PropertyType)
    image = models.ImageField(upload_to="property/images/")
    city = models.CharField(max_length = 40)
    property_name = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.property_name

class Review(models.Model):
    name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to="property/images/")
    description = models.TextField()
    
    def __str__(self):
            return self.name