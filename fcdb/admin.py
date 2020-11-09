from django.contrib.admin import AdminSite

from .models import Parcels

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Parcels)