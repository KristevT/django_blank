from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'max_price', 'min_price')
    readonly_fields = ('id',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'expiration_date', 'is_fine', 'category_id')
    readonly_fields = ('id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)