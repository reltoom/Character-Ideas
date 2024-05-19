from django.shortcuts import render
from django.views import generic
from .models import Character

# Create your views here.
class CharacterList(generic.ListView):
    queryset = Character.objects.filter(status=1)