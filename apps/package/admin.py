from django.contrib import admin
from . models import * 


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'heading', 'updated_at', 'created_at']


class PackageCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'days', 'persons', 'image', 'prices', 'description', 'updated_at', 'created_at']


admin.site.register(Package, PackageAdmin)
admin.site.register(PackageCard, PackageCardAdmin)