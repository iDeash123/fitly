from django.contrib import admin
from .models import Product, Category, ProductImage, Size, ProductSize


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    
    
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
    

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'price') 
    list_filter = ('color', 'category')
    search_fields = ('name', 'description', 'color')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}