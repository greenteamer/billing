# -*- coding: utf-8 -*-
#!/usr/bin/env python
from celery.task import periodic_task
from datetime import timedelta
from celery.schedules import crontab
from datetime import datetime
# from celery.task import
from main.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from project.settings import ADMIN_EMAIL
import datetime

# @periodic_task(run_every = timedelta(seconds = 60))
@periodic_task(ignore_result=True, run_every=crontab(hour=11, minute=00))
def test():

    users = UserProfile.objects.all()
    for user in users:
        user.billing = user.billing - (user.tarif.price/30)
        user.save()

        if user.billing < 26:
            """отправка писем"""
            subject = u'оплата хостинга %s %s' % (user.firstName, user.lastName)
            message = u'Клиент %s %s \n Остаток на счету: %s \n телефон: %s \n e-mail: %s ' % (user.firstName, user.lastName, user.billing, user.phone, user.email)
            send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

        print "%s - %s" % (user.lastName, user.billing)

@periodic_task(ignore_result=True, run_every=crontab(hour=11, minute=00))
def happyBirthday():

    users = UserProfile.objects.all()
    today = datetime.date.today()
    for user in users:

        if user.birthday.month == today.month:
            if user.birthday.day == today.day:
                """отправка писем"""
                subject = u'С днем рождения %s %s' % (user.firstName, user.lastName)
                message = u'%s %s поздравляем с днем рождения тел. %s' % (user.firstName, user.lastName, user.phone)
                send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

        print "%s - %s" % (user.lastName, user.billing)
