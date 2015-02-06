#coding: utf-8
from django.contrib import admin
from main.models import *
from main.forms import *

class PageAdmin(admin.ModelAdmin):
    model = Pages
    prepopulated_fields = {'slug':('name',)}

class RegistratorAdmin(admin.StackedInline):
    model = PropertyRegistrator

class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    inlines = [RegistratorAdmin]
    search_fields = ['site', 'firstName', 'lastName']


admin.site.register(Pages, PageAdmin)
admin.site.register(Block)
admin.site.register(Order)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Registrator)
admin.site.register(Tarif)
