from django.shortcuts import render
from django.Http import HttpResponse

# Create your views here.
def room(request, code):
    return HttpResponse('hi')