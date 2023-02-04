from django.urls import path
from .views import show_map

urlpatterns = [
    path('', show_map, name='home'),
]