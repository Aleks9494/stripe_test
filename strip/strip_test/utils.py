import stripe
from django.conf import settings
from currency_converter import CurrencyConverter


def create_session(data_from_db, email, discount, currency):
    line_items = []
    c = CurrencyConverter()
    for item in data_from_db:
        data = {
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': item.name
                },
                'unit_amount': int(item.price)*100 if currency == 'usd'
                else int(c.convert(item.price, 'USD', 'EUR'))*100,
            },
            'quantity': 1,
            }
        line_items.append(data)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if discount:
        stripe.Coupon.create(duration=discount.duration, id=discount.name, percent_off=discount.percent_off)
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url="http://localhost:4242/success.html",
        cancel_url="http://localhost:4242/cancel.html",
        customer_email=email,
        discounts=[{
            'coupon': discount.name,
        }] if discount else None
    )
    if discount:
        stripe.Coupon.delete(discount.name)
    return session
