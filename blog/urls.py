from django.urls import path, include
from blog.views import post_list , category_list, post_detail

urlpatterns = [
                path('list/', post_list),
                path('category/list/', category_list),
                path('detail/<str:post_title>/', post_detail),
                path('archieve/<int:year>/', post_list)
               ]





