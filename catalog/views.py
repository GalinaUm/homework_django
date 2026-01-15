from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from catalog.forms import ProductForm
from catalog.models import Product, Category


def home(request):
    return render(request, 'home.html')


def contacts(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h1>Спасибо {name}!</h1>"
            f"<h2>Ваше сообщение получено.</h2>"
            f'<p>"{message}"</p>'
            f"<p>С вами свяжутся по этому <b>{phone}</b> номеру.</p>"
        )

    return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product


# def products_list(request):
#     limit, offset = int(request.GET.get('limit', 9)), int(request.GET.get('offset', 0))
#     products = Product.objects.all()[offset:offset+limit]
#     context = {"products": products}
#     return render(request, 'products_list.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)


def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        purchase_price = request.POST.get("purchase_price")
        image = request.FILES.get("image")

        category = get_object_or_404(Category, id=category_id)

        product = Product.objects.create(
            name=name,
            description=description,
            category=category,
            purchase_price=purchase_price,
            image=image,
        )
        context = {"product": product}
        return render(request, "product_details.html", context)

    return render(request, "product_create.html", {"form": ProductForm()})









