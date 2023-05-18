from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products= Product.objects.all()


    #search code
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains= item_name)

    #paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
    }

    return render(request, 'shop/index.html', context)


def detail(request, id):

    product_object = Product.objects.get(id = id)

    context = {
        'product_object': product_object,
    }
    return render(request, 'shop/detail.html', context)