from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, product_details, product_create

app_name = CatalogConfig.name


urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', products_list, name='products_list'),
    path('catalog/<int:pk>/', product_details, name='product_details'),
    path('catalog/create/', product_create, name='product_create'),
]
