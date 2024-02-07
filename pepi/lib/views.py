from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Главнейшая из страниц")

def cat(request):
    return HttpResponse("cat")
