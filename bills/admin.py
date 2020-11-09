from django.contrib import admin
from .models import TaxBill
class BillAdmin(admin.ModelAdmin):
	list_display=('parcel_id','tax_year','tax_type')
	pass 

# Register your models here.
admin.site.register(TaxBill, BillAdmin)