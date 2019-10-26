from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here


def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")
