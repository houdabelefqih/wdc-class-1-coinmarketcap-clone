from django.shortcuts import render
from .models import Cryptocurrency

import django

django.setup()


# Create your views here.
def display_cryptocoins(request):
    order_param = request.GET.get('order_param', 'rank')
    order_direction = request.GET.get('order_direction', 'asc')
    order_by = 'rank'

    coins = Cryptocurrency.objects.all()
    print(coins)

    search = request.GET.get('search')
    if search:
        coins = coins.filter(name__icontains=search)

    if order_param == 'price':
        order_by = 'price_usd'
    if order_direction == 'desc':
        order_by = '-' + order_by

    coins = coins.order_by(order_by)

    return render(request, 'cryptocoins.html', {
        'order_param': order_param,
        'order_direction': order_direction,
        'coins': coins
    })
