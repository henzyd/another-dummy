from django.contrib import admin
from . import models

# Register your models here.
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added', 'id']
    
admin.site.register(models.ImageModel, ImageModelAdmin)
