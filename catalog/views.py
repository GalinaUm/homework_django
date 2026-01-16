from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Category, Contact


class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h1>Спасибо {name}!</h1>"
            f"<h2>Ваше сообщение получено.</h2>"
            f'<p>"{message}"</p>'
            f"<p>С вами свяжутся по этому <b>{phone}</b> номеру.</p>"
        )


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "category", "purchase_price", "image",)
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "category", "purchase_price", "image",)
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")









