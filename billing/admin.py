from django.contrib import admin

# Register your models here.
from .models import BillingItem

class BillingItem_Admin(admin.ModelAdmin):
    list_display=('item_name','number_1','number_2','total')
    list_display_links=('item_name','number_1','number_2','total')


admin.site.register(BillingItem,BillingItem_Admin)