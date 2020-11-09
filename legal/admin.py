from django.contrib import admin
from .models import TaxForeclosure
class TaxForeclosureAdmin(admin.ModelAdmin):
	pass 


admin.site.register(TaxForeclosure,TaxForeclosureAdmin)
