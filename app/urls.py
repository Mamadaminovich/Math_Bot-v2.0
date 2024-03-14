from django.urls import path
from .views import bot_view, home

urlpatterns = [
    path('', home, name='home'),
    path('bot/', bot_view, name='bot'),
]