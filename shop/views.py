from django.shortcuts import render
from .models import Product, Order
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

def checkout(request):

    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zipcode = request.POST.get("zipcode","")
        total = request.POST.get("total","")


        order = Order(items = items, name= name, email = email, address = address, city= city, state = state, zipcode = zipcode, total = total)
        order.save()


    return render(request, 'shop/checkout.html')