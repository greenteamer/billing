# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns('country.views',
    # url(r'^$', 'country_list_view',
    #     {'template_name':'country/country_list.html'},
    #     name='country'),
    #
    # url(r'^(?P<slug>[-\w]+)/$', 'country_view',
    #     {'template_name':'country/country.html'},
    #     name='country'),
    # Просмотр товара
    # url(r'^product/(?P<product_slug>[-\w]+)/$', 'product_view',
    #     {'template_name':'catalog/product.html'},
    #     name='catalog_product'),
)
