from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 5


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:list')
