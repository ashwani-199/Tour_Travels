from django.db import models

# Create your models here.
class Destination(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class DestinationCard(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='destination', null=True, blank=True)
    discount = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.location