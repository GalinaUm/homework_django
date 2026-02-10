from itertools import product

from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import ProductForm, CategoryForm


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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse('catalog:product_details', args=[self.kwargs.get('pk')])


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    permission_required = 'catalog:product_delete'
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        is_owner = product.owner == user
        is_moderator = user.groups.filter(name='moderator').exists() or user.is_staff
        return is_owner or is_moderator


class CategoryCreateViews(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:product_list")

class CategoryUpdateViews(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:category_list")

class CategoryListViews(LoginRequiredMixin, ListView):
    model = Category







