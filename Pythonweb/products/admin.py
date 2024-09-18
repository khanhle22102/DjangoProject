from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['title', 'id']
admin.site.register(Product, ProductAdmin)
# Register your models here.
