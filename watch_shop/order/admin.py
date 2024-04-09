from django.contrib import admin
from .models import Order, OrderItem, Delivery, Payment

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)
admin.site.register(Payment)
