from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product


def pagesNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс! Такой страницы нет</H1>')  # функция для генерации исключения


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug, cart_product_form=None):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'catalog/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})
