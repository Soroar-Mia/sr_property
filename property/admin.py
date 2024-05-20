from django.contrib import admin

# Register your models here.
from . import models

class PurposeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
class PropertyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('location',), }
    
admin.site.register(models.Purpose, PurposeAdmin)
admin.site.register(models.PropertyType, PropertyTypeAdmin)
admin.site.register(models.Property, PropertyAdmin)
admin.site.register(models.Review)