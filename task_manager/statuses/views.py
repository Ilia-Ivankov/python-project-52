from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class StatusesIndexView(ListView):
    template_name = ''