from django.urls import path
from market.views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
]
