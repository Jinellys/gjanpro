from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='ФИО')
    nick_name = models.CharField(max_length=50, db_index=True, verbose_name='Ник')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, null=True)
    email_address = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Покупатель'

    def __str__(self):
        return self.name

