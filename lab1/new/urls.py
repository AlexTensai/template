from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('categories', views.all_category),
    path('categories/<int:id>', views.category_by_id_get),
    path('categories/<int:id>/delete', views.category_by_id_delete),
    path('categories/create', views.category_by_id_create),
    path('categories/delete', views.category_by_id_delete),
    path('products', views.all_product),
    path('products/<int:id>', views.product_by_id_get),
    path('products/create', views.product_by_id_create),
]