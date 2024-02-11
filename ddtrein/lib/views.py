from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def creatе_library(request):
    return render(request, 'lib/creatе_library.html', {'': 2})