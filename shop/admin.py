from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available_display','created','updated','category']
    list_editable = ['price','stock','available_display','available_order']

# 화면을 CategoryAdmin으로 구성

admin.site.register(Product, ProductAdmin)
