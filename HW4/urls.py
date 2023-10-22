"""
URL configuration for HW4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

app_name = 'HW4'

urlpatterns = [
    path('', views.index, name='index'),
     # Путь для создания клиента
    path('create-client/', views.create_client_view, name='create_client'),
    # Путь для создания товара
    path('create-product/', views.create_product_view, name='create_product'),
    # Путь для создания заказа
    path('create-order/', views.create_order_view, name='create_order'),
    path('client_ordered_products/<int:client_id>/<str:time_period>/', views.client_ordered_products, name='client_ordered_products'),
    # Вы можете передавать параметр time_period в URL, чтобы отображать список товаров за последние 7 дней, 30 дней или 365 дней.
]
