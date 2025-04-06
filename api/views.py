from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Food, Order
from .serializers import CategorySerializer, FoodSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly  

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]  

class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminOrReadOnly]  

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 


