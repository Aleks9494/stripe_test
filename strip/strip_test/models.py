from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

DISCOUNT_DURATION_CHOICES = (
    ("once", "once"),
    ("forever", "forever"),
    ("repeating", "repeating"),
)

CURRENCY_CHOICES = [
    ('eur', 'eur'),
    ('usd', 'usd'),
]


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('strip_test:item', kwargs={'item_id': self.pk})


class Discount(models.Model):
    name = models.CharField(max_length=20)
    duration = models.CharField(choices=DISCOUNT_DURATION_CHOICES, max_length=100)
    percent_off = models.IntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ['name']


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    discount = models.ForeignKey(Discount, related_name='orders', on_delete=models.CASCADE,
                                 verbose_name='Скидка', blank=True, null=True)
    currency = models.CharField(max_length=20, verbose_name="Оплата в валюте", choices=CURRENCY_CHOICES,
                                default='usd')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('strip_test:orders', kwargs={'item_id': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    items = models.ForeignKey(Item, related_name='order_items',
                              on_delete=models.CASCADE, verbose_name='Товары')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return '{}'.format(self.pk)
