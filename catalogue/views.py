from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from catalogue.models import Product, ProductType, Category, Brand
from django.db.models import Q
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
    
    product = Product.objects.select_related('category').all()
    context = "\n".join([f"{product.title}, {product.upc}, {product.category.name}"])
    return HttpResponse(context)
    
    # return HttpResponse(f"new product is: {new_product.title}")


def product_detail(request, pk):
    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        product = queryset.first()
        return HttpResponse(f"title: {product.title}")
    return HttpResponseNotFound("Category does not exist")
    
    
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
