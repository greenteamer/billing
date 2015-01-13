# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import template
from django.contrib.flatpages.models import FlatPage
from django.template import context

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext

"""send mail"""
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from project.settings import ADMIN_EMAIL

from slider.models import *
from feedback.forms import *
from feedback.models import *


register = template.Library()


# @register.inclusion_tag("flexslider.html")
# def categories_tree(request):
# 	"""Возвращает дерево категорий"""
# 	return {'nodes': Category.objects.filter(is_active=True) }


def slider(context, request):
    slides = Slider.objects.all()
    return {
        # 'products': products,
        'slides': slides,
    }
register.inclusion_tag('slider/slider.html', takes_context=True)(slider)

def contactForm_tag(context, request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            order = Contact()
            order.name = request.POST['name']
            order.phone = request.POST['phone']
            order.email = request.POST['email']
            destination = CountryDestination.objects.get(id=request.POST['destination'])
            order.destination = destination
            order.save()

            # """отправка писем"""
            subject = u'prima-tours.org заявка от %s' % order.name
            message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n направление: %s \n e-mail: %s ' % (order.id, order.name, order.phone, order.destination, order.email)
            send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

        else:
            form = ContactForm(request.POST)
            return {
                'form':form,
                'error':form.errors,
            }

    else:
        form = ContactForm()
        return {
            'form':form,
        }
register.inclusion_tag('feedback/contact_tag.html', takes_context=True)(contactForm_tag)

def contactFormMini_tag(context, request):
    if request.method == 'POST':
        form = ContactFormMini(request.POST)
        if form.is_valid:
            subject = u'prima-tours.org заявка от %s' % request.POST['name']
            message = u'Имя: %s \n телефон: %s' % (request.POST['name'], request.POST['phone'])
            send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)
        else:
            form = ContactFormMini(request.POST)
            return {
                'form':form,
                'error':form.errors,
            }
    else:
        form = ContactFormMini()
        return {
            'form':form,
        }
register.inclusion_tag('feedback/contact_mini_tag.html', takes_context=True)(contactFormMini_tag)