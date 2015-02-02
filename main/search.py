# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db.models import Q

from main.models import *


STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
               'of','on','or','that','the','to','with']

def users(search_text):
    """Извлекает товары содержащие указанный текст"""

    words = _prepare_words(search_text)
    profiles = UserProfile.objects.all()

    # Проходим по всем словам в поисковом запросе
    # получаем все товары при совпадении с брендом
    # for word in words:
    #     brands = brands.filter(Q(name__icontains=word))
    #     for brand in brands:
    #         products_of_brands = products.filter(brand_name=brand)
    #         results.extend(products_of_brands)

    # Проходим по всем словам в поисковом запросе
    # получаем все товары по совпадению с описанием или названием
    for word in words:
        profiles = profiles.filter(
            Q(firstName__icontains=word) |
            Q(lastName__icontains=word) |
            Q(site__icontains=word)
        )



    return profiles


def _prepare_words(search_text):
    """Удаляет общие слова перечисленные с списке STRIP_WORDS
    Делает срез поисковой фразы до 5 слов"""
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]
