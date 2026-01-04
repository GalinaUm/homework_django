from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


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


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)



