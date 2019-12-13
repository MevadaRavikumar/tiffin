from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu_categories(request):
    return render (request, 'menu-categories.html')

def single_categories(request):
    return render (request, 'single-categories.html')