from django.db import models
from django.db.models import PROTECT
from catalog.models import Product
from clients.models import Client


class Payment(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = 'Способ оплаты'

    def __str__(self):
        return self.name


class Delivery(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = 'Способ достаки'

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment = models.ForeignKey(Payment, on_delete=PROTECT, verbose_name='Способ оплаты')
    delivery = models.ForeignKey(Delivery, on_delete=PROTECT, verbose_name='Способ доставки')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Заказы'

    # def __str__(self):
    #     return 'Order {}'.format(self.id)

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.client.name}"


class OrderItem(models.Model):
#хранит продукт, количество и цену, уплаченную за каждый товар
#    objects = None
    order = models.ForeignKey(Order, on_delete=PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=PROTECT, related_name='order_items')
    price = models.ForeignKey(Product, on_delete=PROTECT, related_name='price_items')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    def __str__(self):
        return 'Order {}'.format(self.id)


    # def __str__(self):
    #     return f"Товар {self.name} | Заказ № {self.pk}"

    def get_cost(self):
#возврат стоимости товара
        return round(self.product.sell_price() * self.quantity)



