from django.db import models

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class PackageCard(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    days = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='Pakages', null=True, blank=True)
    persons = models.CharField(max_length=100, null=True, blank=True)
    prices = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.location
    