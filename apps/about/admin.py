from django.contrib import admin
from .models import *



class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'heading', 'paragraph_1', 'paragraph_2', 'image', 'updated_at', 'created_on']

class AboutFeaturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'list_text', 'updated_at', 'created_on']

admin.site.register(About, AboutAdmin)
admin.site.register(AboutFeatures, AboutFeaturesAdmin)