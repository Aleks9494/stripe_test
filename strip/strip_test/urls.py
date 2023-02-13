from django.urls import path

from .views import *

app_name = 'strip_test'
urlpatterns = [
    path('items/<int:item_id>/', ShowItem.as_view(), name='item'),
    path('items', ShowItems.as_view(), name='items'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('config/', stripe_config),
    path('order/', CreateOrder.as_view(), name='order'),
    path('order/<int:order_id>/', MyOrder.as_view(), name='orders'),
    path('order/<int:order_id>/buy/', buy_items, name='buy_items'),
    path('success/', SuccessView.as_view()),
    path('cancel/', CancelledView.as_view()),
]