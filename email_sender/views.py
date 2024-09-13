from urllib import request
from django.shortcuts import render

# Create your views here.

def base_view(render):
    return render(request, 'templates/base.html')