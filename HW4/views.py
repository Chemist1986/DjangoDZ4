from django.shortcuts import render, redirect
from django.http import HttpResponse
from .crud import create_client, create_product, create_order
from .models import Client, Order, Product
from .forms import ClientForm, ProductForm, OrderForm, ClientTimePeriodForm
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse

# Пример представления для создания клиента
def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            registration_date = timezone.now()
            client = create_client(name, email, phone_number, address, registration_date)
            return HttpResponse(f'Клиент {client.name} успешно создан!')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

# Пример представления для создания товара
def create_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            # Предположим, что 'photo' - это имя поля для загрузки файла в вашей форме ProductForm
            photo = form.cleaned_data['photo']
            date_added = timezone.now()
            product = create_product(name, description, price, quantity, date_added, photo)
            return HttpResponse(f'Продукт {product.name} успешно создан!')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

# Пример представления для создания заказа
def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            products = form.cleaned_data['products']
            total_amount = form.cleaned_data['total_amount']
            order_date = form.cleaned_data['order_date']
            order = create_order(client, products, total_amount, order_date)
            return HttpResponse(f'Order for {order.client.name} created successfully!')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

def client_ordered_products(request, client_id, time_period):
    if request.method == 'POST':
        form = ClientTimePeriodForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            time_period = form.cleaned_data['time_period']

            # Осуществите выборку товаров заказанных клиентом за указанный временной период
            # Используйте переменные client и time_period для фильтрации данных

            # Пример фильтрации по временному периоду
            if time_period == '7days':
                # Ваш код для фильтрации за последние 7 дней
                pass
            elif time_period == '30days':
                # Ваш код для фильтрации за последние 30 дней
                pass
            elif time_period == '365days':
                # Ваш код для фильтрации за последние 365 дней
                pass

            # Отобразите результаты на странице
            return render(request, 'client_ordered_products.html', {'client': client, 'time_period': time_period, 'ordered_products': ordered_products})
    else:
        form = ClientTimePeriodForm()
    return render(request, 'client_ordered_products_form.html', {'form': form})

def index(request):
    client_id = 1
    return render(request, 'index.html', {'client_id': client_id})
