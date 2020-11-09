from django.contrib import admin
from .models import TaxContract
class TaxContractAdmin(admin.ModelAdmin):
	pass 


admin.site.register(TaxContract,TaxContractAdmin)