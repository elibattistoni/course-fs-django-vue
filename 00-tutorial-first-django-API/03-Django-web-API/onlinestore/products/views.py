from django.http import JsonResponse

from .models import Manufacturer, Product

#! let's use function based views to make the code as explitic as possible
def product_list(request):
    products = Product.objects.all()
    # convert the products query set to a json object
    # with pk and name you select specific properties of the product object
    # print(products.values())
    # print(products.values("pk", "name"))
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    #! NB IMPORTANT this is not the best way of delivering information to UI clients!
    #! so the JsonResponse class is very useful, but it may not work for real world scenarios
    #! NB this is wy we usually use the ' DJANGO REST FRAMEWORK '
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)

        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }

        response = JsonResponse(data)

    except Product.DoesNotExist:
        response = JsonResponse(
            {"error": {"code": 404, "message": "product not found!"}}, status=404
        )
        #! NB the status is important info for the client (frontend) to know that a product was not found
        #! the json part provides more information for us humans

    return response


"""
# (from 02-Django-refresh)
#! NB the ones below are class based views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "products/product_lsit.html"
"""
