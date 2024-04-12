# admin.py

from django.contrib import admin
from .models import Contact
from .models import Voter

admin.site.register(Contact)
admin.site.register(Voter)