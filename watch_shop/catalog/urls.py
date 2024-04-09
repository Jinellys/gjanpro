from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('product_detail/', views.product_detail, name='product_detail'),
]
