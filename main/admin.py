#coding: utf-8
from django.contrib import admin
from main.models import *

class PageAdmin(admin.ModelAdmin):
    model = Pages
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Pages, PageAdmin)
admin.site.register(Block)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(Tarif)
