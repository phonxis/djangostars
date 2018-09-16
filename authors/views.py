from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    CreateView
)

from .models import Author
from .forms import AuthorForm


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('books:create')
