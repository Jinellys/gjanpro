
from other import views
from django.urls import path

app_name = 'other'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='Добро пожаловать в WatchShop!'),
    path('about/', views.about, name='about'),

]