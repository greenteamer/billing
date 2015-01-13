# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.db import models
from ckeditor.fields import RichTextField

class Slider(models.Model):
    name  = models.CharField(verbose_name=u'Название слайдера', max_length=100)
    # text = RichTextField()
    image = models.ImageField(verbose_name=u'Фото', upload_to='flexslider')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = (u'Слайдер на главной')
        verbose_name = (u'Слайд')