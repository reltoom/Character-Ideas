from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_idea(request):
    return HttpResponse("My character idea will be here!")