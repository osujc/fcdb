from django.contrib import admin
from .models import Parcel, ParcelGroup

class ParcelAdmin(admin.ModelAdmin):
	list_display=('parcel_id','parcel_address','parcel_city')
	list_display_links = ('parcel_id','parcel_address')
	search_fields = ('parcel_id','parcel_address')
	list_per_age = 100

class MembershipAdmin(admin.ModelAdmin):
	list_display = ('parcel','parcel_group')
	list_display_links = ('parcel','parcel_group')
	search_fields = ('parcel','parcel_group')
	list_per_age = 100
	

admin.site.register(Parcel, ParcelAdmin)
admin.site.register(ParcelGroup)
#admin.site.register(GroupMembership, MembershipAdmin)