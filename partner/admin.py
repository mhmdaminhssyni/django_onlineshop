from django.contrib import admin
from partner.models import Partner, PartnerStock
from django.contrib.admin import register
# Register your models here.

@register(PartnerStock)
class PartnerStockAdmin(admin.ModelAdmin):
    list_display = ['partner', 'product', 'price']
    
@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']