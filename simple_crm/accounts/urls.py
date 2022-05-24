from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer/<slug:slug>/', views.customer, name='customer'),
    path('create_order/<slug:slug>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
]
