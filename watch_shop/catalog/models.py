from django.db import models
from django.db.models import PROTECT


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = 'пол'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    article_number = models.CharField(max_length=20, db_index=True, null=True)
    category = models.ForeignKey(Category, on_delete=PROTECT)
    brand = models.ForeignKey(Brand, on_delete=PROTECT)
    gender = models.ForeignKey(Gender, on_delete=PROTECT)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name='Наличие')
    stock = models.PositiveIntegerField(verbose_name='Остаток')

    class Meta:
        ordering = ('name',)  # сортирока по названию дефолтно
        index_together = (('id', 'slug'),)  # составной индекс для поиска и сортировки по комбинации этих полей
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.name





