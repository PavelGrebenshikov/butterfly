from django.shortcuts import render
from django.http import request

# Create your views here.

def index(reqeust):
    return render(request, 'home/index.html', context=None)