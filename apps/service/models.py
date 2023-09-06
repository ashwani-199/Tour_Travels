from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class ServiceCard(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='service', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.heading