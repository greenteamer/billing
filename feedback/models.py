# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from country.models import *

class Contact(models.Model):
    name = models.CharField(verbose_name=u'Имя', max_length=100)
    phone = models.CharField(verbose_name=u'Телефон', max_length=11)
    email = models.EmailField(verbose_name=u'e-mail', max_length=30)

    destination = models.ForeignKey(CountryDestination, verbose_name=u'Направление')

    def __unicode__(self):
        return '%s заявка на %s' % (self.name, self.destination.name)

