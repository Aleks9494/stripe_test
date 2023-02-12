from django.contrib import admin
from .models import Item, OrderItem, Order, Discount


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'percent_off')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['items']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'created', 'discount']
    list_filter = ['email']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Discount, DiscountAdmin)
