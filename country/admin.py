#coding: utf-8
from django.contrib import admin
from country.models import *

class CountryImageAdmin(admin.StackedInline):
    model = CountryImage
    extra = 1

class CountryDestinationAdmin(admin.StackedInline):
    model = CountryDestination
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    model = Country
    fieldsets = [
        (u'Основная информация', {'fields':['name','slug','body']}),
        (u'Специальная информация', {'fields': ['special_image','special_body']}),
    ]
    inlines = [CountryImageAdmin, CountryDestinationAdmin]
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Country, CountryAdmin)