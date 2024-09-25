from operator import index

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogHomeView, CatalogContactsView, CatalogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', CatalogHomeView.as_view(), name='home'),
    path('contacts/', CatalogContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', CatalogDetailView.as_view(), name='product_detail')

    ]