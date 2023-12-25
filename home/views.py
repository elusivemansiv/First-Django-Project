from django.shortcuts import render
from  django.http import HttpResponse

def index_1(request):
    return HttpResponse("<h1>Home</h1>")
