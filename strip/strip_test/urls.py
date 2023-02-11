from django.urls import path

from .views import *

app_name = 'strip_test'
urlpatterns = [
    path('items/<int:item_id>/', ShowItem.as_view(), name='item'),
    path('items', ShowItems.as_view(), name='items'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('config/', stripe_config)
]