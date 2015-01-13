# -*- coding: utf-8 -*-
#!/usr/bin/env python
#import urllib
import random
from django.core import urlresolvers
from main.models import *


def process(request):

    transaction_id = random.randint(1, 999999)
    order = create_order(request, transaction_id)

    """считаем текущую сумму на счете пользователя"""
    user = order.user
    billing = calculate(order)
    user.billing = billing

    results = {'order_number': order.id, 'order': order}


    order.save()
    user.save()

    return results


def create_order(request, transaction_id):

    order = Order()
    order.transaction_id = transaction_id
    order.money = request.POST['money']
    user = User.objects.get(id=request.POST['user'])
    userProfile = UserProfile.objects.get(user=user)
    order.user = userProfile

    return order


def calculate(order):
    billing = order.user.billing + int(order.money)

    return  billing