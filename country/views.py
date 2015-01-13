# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from country.models import *

# Create your views here.

def country_list_view(request, template_name="country/country_list.html"):
    country_list = Country.objects.all()
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))

def country_view(request, slug, template_name="country/country.html"):
    country = Country.objects.get(slug=slug)
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))