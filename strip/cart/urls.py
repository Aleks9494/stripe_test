from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/<int:item_id>/', cart_add, name='cart_add'),
]
