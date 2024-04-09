from django.db import models
from django.db.models import PROTECT

from catalog.models import Product

from clients.models import Client


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=PROTECT, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=PROTECT, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзину"
        verbose_name_plural = "Корзина"

#    objects = CartQueryset().as_manager()

    # def products_price(self):
    #     return round(self.product.price * self.quantity, 2)

    def __str__(self):
        if self.client:
            return f'Корзина {self.client.name} | Товар {self.product.name} | Количество {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'