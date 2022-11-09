from django.urls import path
from .views import getmeta

urlpatterns = [
    path('meta/', getmeta),
]
