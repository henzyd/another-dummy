from django.shortcuts import render
from . import models


def home_page(request):
    images = models.ImageModel.objects.all()
    context = {
        'images': images
    }
    return render(request, 'my_app/index.html', context) 
