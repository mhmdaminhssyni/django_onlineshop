from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from catalogue.models import Product, ProductType, Category, Brand
from django.db.models import Q
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from transaction.models import UserScore
import os
# Create your views here.

def products_list(request):
    # products = Product.objects.all()
    
    # product_type = ProductType.objects.filter(title='phone')
    # category = Category.objects.filter(name='Electricity')
    
    # new_product = Product.objects.create(
    #     product_type=product_type,
    #     title='redmi note 13',
    #     upc=2957,
    #     category=category,
    #     is_active=False
        
    # )
    
    context = dict()
    context['products'] = Product.objects.select_related('category').all()
    return render(request, 'catalogue/product_list.html', context=context)
    
    # return HttpResponse(f"new product is: {new_product.title}")


def product_detail(request, pk):
    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        context = dict()
        context['product'] = queryset.first()
        
        return render(request, 'catalogue/product_detail.html', context=context)
    #   return HttpResponse(f"title: {product.title}")
    # return HttpResponseNotFound("Category does not exist")
    raise Http404('not found')
    
def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponseNotFound("Category does not exist")
    

    product_ids = [1, 2, 3]
    products = Product.objects.filter(id__in=product_ids)
    
    # products = Product.objects.filter(category__name = name)
    
    context = "\n".join([f"{product.title}, {product.upc}" for product in products])
    return HttpResponse(context)
    
def products_search(request):
    title = request.GET.get('q')
    products = Product.objects.actives(title__icontains=title,
                                      category__name__icontains=title
                                    #   title__istartswith=title
                                      )
    context = "\n".join([f"{product.title}, {product.upc}" for product in products])

    return HttpResponse(f"search page, {context}")

@login_required()
@require_http_methods(['GET'])
# @user_passes_test(check_is_active)
@permission_required('transaction.has_permission_scores')
def user_profile(request):
    return HttpResponse(f"hello {request.user.username}")


@login_required
@require_POST
def campaign(request):
    return HttpResponse(f"hello {request.user.username}")