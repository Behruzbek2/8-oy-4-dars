from django.urls import path
from .views import CategoryListCreateView, FoodListCreateView, OrderListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('foods/', FoodListCreateView.as_view(), name='food-list'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
]
