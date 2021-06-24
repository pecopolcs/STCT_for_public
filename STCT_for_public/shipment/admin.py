from django.contrib import admin
from .models import InfoModel

class InfoAdmin(admin.ModelAdmin):
    list_display = ('consignee', 'shipper_name', 'depdate_from_ru',
        'spec_no', 'cntr_no', 'item_property', 'cube_m3', 'cntr_eta',
        'vessel_name', 'bool_eta', 'final_update', 'option')
    ordering = ('consignee',)
    list_filter = ('bool_eta', 'consignee', 'shipper_name',)
    #search_fields = ('consignee', 'shipper_name', 'depdate_from_ru',
    #    'spec_no', 'cntr_no', 'item_property', 'cube_m3', 'cntr_eta',
    #    'vessel_name', 'final_update', 'option')

admin.site.register(InfoModel, InfoAdmin)