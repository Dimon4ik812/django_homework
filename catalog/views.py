from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base.html', context=context)

def contacts(request):
        if request.method == 'POST':
            # Получение данных из формы
            name = request.POST.get('name')
            message = request.POST.get('message')
            # Обработка данных (например, сохранение в БД, отправка email и т. д.)
            # Здесь мы просто возвращаем простой ответ
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return render(request, 'contacts.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context=context)
