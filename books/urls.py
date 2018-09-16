from django.urls import path

from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView
)


app_name = 'books'  # need for include function in root urls.py

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('book/create/', BookCreateView.as_view(), name='create'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='update'),
]
