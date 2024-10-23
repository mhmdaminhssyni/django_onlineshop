from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def catalogue_list(request):
    return HttpResponse("catalogue list page")

def category_list(request):
    return HttpResponse("category list page")

def catalogue_detail(request, catalogue_title):
    return HttpResponse(f"catalogue detail page for {catalogue_title}")