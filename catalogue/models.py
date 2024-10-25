from django.db import models

# Create your models here.
class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    
    
class ProductAttribute(models.Model):
    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)