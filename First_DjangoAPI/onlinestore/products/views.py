from django.http import JsonResponse

from .models import Product,Manufacturer

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values("pk","name"))}
    response = JsonResponse(data)
    return response

def product_detail(request, pk_product):
    try:
        product = Product.objects.get(pk=pk_product)
        data = {"product":{
                    "name":product.name,
                    "manufacturer":product.manufacturer.name,
                    "description":product.description,
                    "photo":product.photo.url,
                    "price":product.price,
                    "shipping_cost":product.shipping_cost,
                    "quantity":product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code":404,
                "message":"product not found!!"
            }}, status=404)
    return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(activate=True)
    data = {"manufacturer": list(manufacturers.values())}
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk_manufacturer):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk_manufacturer)
        manufacturer_products = manufacturer.products.all()
        
        data = {"manufacturer":{
                    "name":manufacturer.name,
                    "location":manufacturer.location,
                    "active":manufacturer.activate,
                    "products":list(manufacturer_products.values()),
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code":404,
                "message":"manufacturer not found!!"
            }}, status=404)
    return response