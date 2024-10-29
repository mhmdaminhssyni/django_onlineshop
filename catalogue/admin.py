from django.contrib import admin
from catalogue.models import Category, Brand, Product, ProductType, ProductAttribute
from django.contrib.admin import register
# Register your models here.
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','product_type', 'upc', 'is_active', 'category', 'brand')
    list_editable = ('is_active', )
    list_display_links = ['brand']
    list_filter = ['is_active']
    search_fields = ['title', 'brand__name']
    actions = ['active_all']
    
    def active_all(self, request, queryset):
        pass

@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'create_time']
    inlines = [ProductAttributeInline]


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type']
    


admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductType, ProductTypeAdmin)
