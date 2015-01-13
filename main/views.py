# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
# from project.settings import *

"""send mail"""
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from project.settings import ADMIN_EMAIL

from main.models import *
from feedback.forms import *
from feedback.models import *
from main.models import *
from main.operation import *
from main.search import *
# Create your views here.

def home_view(request, template_name="main/home.html"):
    front_pages = Pages.objects.filter(is_aqua=True)
    block_text = get_object_or_404(Block, is_main=True)
    # users = User.objects.all()
    # users_is_staff = User.objects.filter(is_staff=0)
    # static = STATIC_ROOT
    # path = MEDIA_ROOT
    if request.user.is_superuser:
        profiles = UserProfile.objects.all()
    else:
        profiles = None
    form = AddOrderForm()
    form2 = SearchForm()
    if request.method == 'POST':
        postdata = request.POST.copy()

        if postdata.has_key('add'):
            form = AddOrderForm(request.POST)
            if form.is_valid:
                """создание и сохранение операции зачисления денег"""
                """логика в operation.py"""
                order = process(request)

        if postdata.has_key('search'):
            form = SearchForm(request.POST)
            if form.is_valid:
                """поиск по пользователям"""
                if request.user.is_superuser:
                    search_text = request.POST['name']
                    profiles = users(search_text)

        if postdata.has_key('reset'):
            if request.user.is_superuser:
                profiles = UserProfile.objects.all()


    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def page_view(request, slug, template_name="main/page.html"):
    page = get_object_or_404(Pages, slug=slug)
    if slug == 'kontakty':
        if request.method == 'POST':
            form = ContactFormMini(request.POST)
            if form.is_valid():
                # form.clean_phone()
                order = Contact()
                order.name = request.POST['name']
                order.phone = request.POST['phone']
                order.email = request.POST['email']
                destination = CountryDestination.objects.get(id=request.POST['destination'])
                order.destination = destination
                order.save()

                """отправка писем"""
                subject = u'prima-tours.org заявка от %s' % order.name
                message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n направление: %s \n e-mail: %s ' % (order.id, order.name, order.phone, order.destination, order.email)
                send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

            else:
                form = ContactFormMini(request.POST)
                return render(request, 'main/page.html', {
                    'form': form,
                    'error': form.errors,
                })
        else:
            form = ContactFormMini()

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))