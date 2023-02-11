from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Item
import stripe


class ShowItem(DetailView):
    model = Item
    template_name = 'Item.html'
    context_object_name = 'item'
    pk_url_kwarg = "item_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товар - {context["item"].name}'
        return context


class ShowItems(ListView):
    model = Item
    template_name = 'Items.html'
    context_object_name = 'items'
    pk_url_kwarg = "item_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товары'
        return context


def buy_item(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, id=item_id)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "rub",
                            "product_data": {"name": item.name},
                            "unit_amount": item.price,
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url="http://localhost:4242/success.html",
                cancel_url="http://localhost:4242/cancel.html",
            )
            print(session['id'])
            return JsonResponse({'sessionId': session['id']})

        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)})


def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)
