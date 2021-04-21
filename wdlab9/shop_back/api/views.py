from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_details(request, product_id):
    products = Product.objects.filter(pk=product_id)
    if len(products) == 0:
        return JsonResponse({'message': 'No match found'})
    for product in products:
        return JsonResponse(product.to_json())


def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_details(request, category_id):
    categories = Category.objects.filter(pk=category_id)
    if len(categories) == 0:
        return JsonResponse({'message': 'No match found'})
    for category in categories:
        return JsonResponse(category.to_json())

