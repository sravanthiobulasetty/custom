from django.contrib import admin

# Register your models here.

from custom_app.models import *

admin.site.register(User)