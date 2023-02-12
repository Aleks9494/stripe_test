from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView
from .forms import OrderCreateForm
from .models import Item, OrderItem, Order
from cart.cart import Cart
from .utils import create_session


class ShowItem(DetailView):
    model = Item
    template_name = 'Item.html'
    context_object_name = 'item'
    pk_url_kwarg = "item_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товар - {context["item"].name}'
        context['cart'] = Cart(self.request)
        return context


class ShowItems(ListView):
    model = Item
    template_name = 'Items.html'
    context_object_name = 'items'
    pk_url_kwarg = "item_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товары'
        context['cart'] = Cart(self.request)
        return context


class CreateOrder(CreateView):
    template_name = 'create.html'
    form_class = OrderCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Заказ'
        context['cart'] = Cart(self.request)
        return context

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         items=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
        return redirect('strip_test:orders', order_id=order.pk)


class MyOrder(DetailView):
    model = Order
    template_name = 'created.html'
    context_object_name = 'order'
    pk_url_kwarg = "order_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Заказ - {context["order"].pk}'
        return context


def buy_item(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, id=item_id)
        try:
            session = create_session([item], None, None, 'usd')
            return JsonResponse({'sessionId': session['id']})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})


def buy_items(request, order_id):
    if request.method == 'GET':
        items_in_order = OrderItem.objects.filter(order__id=order_id)
        order = Order.objects.get(pk=order_id)
        items = [i.items for i in items_in_order]
        try:
            session = create_session(items, order.email, order.discount, order.currency)
            return JsonResponse({'sessionId': session['id']})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})


def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)
