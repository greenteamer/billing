# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Pages(models.Model):
    name = models.CharField(verbose_name=u'Название страницы', max_length=100)
    slug = AutoSlugField(editable=True)
    image = models.ImageField(verbose_name=u'Изображение', upload_to='pages')

    body = RichTextField()
    is_aqua = models.BooleanField(verbose_name=u'На главную', default=False)

    def __unicode__(self):
        return self.name

    def page_is_main(self):
        return self.is_aqua

class Block(models.Model):
    text = RichTextField()
    is_main = models.BooleanField(verbose_name=u'Блок рядом со слайдером', default=False)

    def block_is_main(self):
        return self.is_main



class BaseOrderInfo(models.Model):
    """Абстрактный класс для заказов"""
    class Meta:
        abstract = True

    # Контактная информация
    firstName = models.CharField(max_length=100, verbose_name=u'Имя пользователя')
    lastName = models.CharField(max_length=100, verbose_name=u'Фамилия пользователя')
    email = models.EmailField(max_length=50, verbose_name=(u'Ваш email'))
    phone = models.CharField(max_length=20, verbose_name=(u'Ваш телефон'))
    city = models.CharField(max_length=50, verbose_name=(u'Город'))

class Tarif(models.Model):
    sites_number = models.IntegerField(max_length=20, verbose_name=u'Колличество сайтов')
    # price = models.IntegerField(max_length=20, verbose_name=u'Стоимость за месяц')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Стоимость за месяц')

    def __unicode__(self):
        return '%s' % self.sites_number

class UserProfile(BaseOrderInfo):
    """Профиль пользователя"""
    user = models.ForeignKey(User, unique=True)
    tarif = models.ForeignKey(Tarif, verbose_name=u'Выбрать тариф')
    site = models.CharField(max_length=100, verbose_name=u'Индетификационный сайт')
    billing = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Счет пользователя')

    def __unicode__(self):
        return u'Профиль: ' + self.user.username

    class Meta:
        verbose_name_plural = u'Профили пользователей'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        get_user = User.objects.get(id=self.user.id)
        get_user.first_name = self.firstName
        get_user.last_name = self.lastName
        get_user.save()
        return super(UserProfile, self).save(force_insert, force_update, using)


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    money = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Сумма на счет')
    user = models.ForeignKey(UserProfile, verbose_name=u'Ввыбрать пользователя')
    transaction_id = models.CharField(max_length=20, verbose_name=u'id операции')
    def __unicode__(self):
        get_user = User.objects.get(id=self.user.user.id)
        return u'%s - %s %s: %s руб.' % (get_user.username, get_user.first_name, get_user.last_name, self.money)
