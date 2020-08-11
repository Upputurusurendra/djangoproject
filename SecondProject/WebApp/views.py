from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_page(request):
    return HttpResponse("<h1>WELCOM TO HOME PAGE</h1>")
def Index_page(request,id):
    return HttpResponse(f"welcome to index_page of-{id}")
