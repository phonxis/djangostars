from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'price', 'authors', 'publish_date')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Title'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'ISBN'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Price'
            }),
            'authors': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '5'
            }),
            'publish_date': AdminDateWidget()
        }
