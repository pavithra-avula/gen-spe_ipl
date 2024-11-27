from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ruthuraj(request):
    return HttpResponse('<h1>ruthuraj is the new captain of CSK</h1>')