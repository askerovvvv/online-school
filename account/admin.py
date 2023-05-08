from django.contrib import admin

from account.models import *

admin.site.register(CustomUser)

admin.site.register(MassEmail)