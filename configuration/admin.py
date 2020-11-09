from django.contrib import admin
from .models import TaxYear, TaxType

class TaxYearAdmin(admin.ModelAdmin):
	pass 

class TaxTypeAdmin(admin.ModelAdmin):
	pass 
# Register your models here.

admin.site.register(TaxYear,TaxYearAdmin)
admin.site.register(TaxType,TaxTypeAdmin)