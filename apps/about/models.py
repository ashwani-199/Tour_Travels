from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=500, null=True, blank=True)
    paragraph_1 = models.CharField(max_length=1000, null=True, blank=True)
    paragraph_2 = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='about', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class AboutFeatures(models.Model):
    list_text = models.CharField(max_length=1000, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.list_text
