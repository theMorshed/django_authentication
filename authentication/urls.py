from django.urls import path
from authentication.views import home

urlpatterns = [
    path('', home, name='homepage'),
]