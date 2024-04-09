from django.contrib import admin
from .models import Product, Brand, Category, Gender


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# @admin.register()
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender)

# python3 manage.py runserver
# python3 manage.py makemigrations
# python3 manage.py migrate
