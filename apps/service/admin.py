from django.contrib import admin
from .models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'heading', 'updated_at', 'created_on']


class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'description', 'image', 'updated_at', 'created_on']


admin.site.register(Services, ServiceAdmin)
admin.site.register(ServiceCard, ServiceCardAdmin)