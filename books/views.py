from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book.html'
