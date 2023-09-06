from django.contrib import admin
from .models import * 

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'heading', 'updated_at', 'created_at']


class DestinationCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'discount', 'image', 'updated_at', 'created_at']

admin.site.register(Destination, DestinationAdmin)
admin.site.register(DestinationCard, DestinationCardAdmin)
