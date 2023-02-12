from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .cart import Cart
from strip_test.models import Item


@require_POST  # метод POST
def cart_add(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.add(product=product)

    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'detail.html', {'cart': cart})
