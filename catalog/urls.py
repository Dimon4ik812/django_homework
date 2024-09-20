from operator import index

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_information, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('info/', product_information, name='product_information'),
    path('product_detail/<int:product_id>', product_detail, name='product_detail')

    ]