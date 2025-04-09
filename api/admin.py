from django.contrib import admin
from .models import Category, Food, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'food', 'quantity', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'food__name')

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Order, OrderAdmin) 
