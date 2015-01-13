# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models

class Country(models.Model):

    name = models.CharField(verbose_name=u'Название страницы', max_length=100)
    slug = AutoSlugField(editable=True, verbose_name=u'создание ссылки')
    body = RichTextField(verbose_name=u'Основное описание')
    # image = models.ImageField(verbose_name=u'Основное фото', upload_to='country')
    special_image = models.FileField(verbose_name=u'Иконка в специальную область', upload_to='country', null=True)
    special_body = RichTextField(verbose_name=u'Описание для специальной области', null=True)

    def get_absolute_url(self):
        return '/country/%s' % self.slug

    def get_country_images(self):
        return CountryImage.objects.filter(country=self)

    def get_country_destinations(self):
        return CountryDestination.objects.filter(country=self)

    def __unicode__(self):
        return self.name


class CountryImage(models.Model):
    image = models.FileField(verbose_name=u'Фото', upload_to='country', )
    country = models.ForeignKey(Country, verbose_name=u'Для какой страны')

    def url(self):
        return '/media/%s' % self.image

    def __unicode__(self):
        return self.country.name

    class Meta:
        verbose_name_plural = u'Галерея страны'
        verbose_name = u'Фото'


class CountryDestination(models.Model):
    name = models.CharField(verbose_name=u'Название направления', max_length=100)
    image = models.FileField(verbose_name=u'Фото для направления', upload_to='country',)
    body = RichTextField(verbose_name=u'Краткое описание')
    body_all = RichTextField(verbose_name=u'Подробное описание')
    country = models.ForeignKey(Country, verbose_name=u'Для какой страны')

    def image_url(self):
        return '/media/%s' % self.image

    def __unicode__(self):
        return '%s - %s' % (self.country.name, self.name)

    class Meta:
        verbose_name_plural = u'Направление по стране'
        verbose_name = u'Направление'
