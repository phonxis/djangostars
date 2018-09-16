from django.urls import path

from .views import (
    AuthorCreateView,
)


app_name = 'authors'  # need for include function in root urls.py

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create'),
]
