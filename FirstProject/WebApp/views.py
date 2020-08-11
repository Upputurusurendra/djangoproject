from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page(request):
    return HttpResponse('<h1>WELCOME TO MY HOME_PAGE</h1>')
def Index_page(request):
    return  HttpResponse("<h2>WELCOME TO MY INDEX_PAGE</h2>")
