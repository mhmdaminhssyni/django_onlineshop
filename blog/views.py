from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
def post_list(request, year):
    return HttpResponse("posts lists page")



def category_list(request):
    return HttpResponse("posts categories list page")

def post_detail(request, post_title):
    return HttpResponse(f"post detail page for post titled: {post_title}")