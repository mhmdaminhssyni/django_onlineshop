from catalogue.views import catalogue_list, category_list,catalogue_detail
from django.urls import path, include
urlpatterns = [
                path('list/', catalogue_list),
                path('categories/list/', category_list),
                path('catalogue/<str:catalogue_title>/', catalogue_detail)
                ]