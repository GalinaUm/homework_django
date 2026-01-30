from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactView, HomeView, CategoryCreateViews, CategoryUpdateViews, CategoryListViews

app_name = CatalogConfig.name


urlpatterns = [
    path('catalog/home/', HomeView.as_view(), name='home'),
    path('catalog/contacts/', ContactView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path("category_create/", CategoryCreateViews.as_view(), name="category_create"),
    path("category/<int:pk>/update", CategoryUpdateViews.as_view(), name="category_update"),
    path("category/", CategoryListViews.as_view(), name="category_list")
]
