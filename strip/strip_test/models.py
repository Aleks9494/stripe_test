from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('strip_test:item', kwargs={'item_id': self.pk})
