# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from main.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
