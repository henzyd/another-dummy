from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.home_page, name='home_page'),
]