from django.http import request
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'upload/home.html')