from django.db import models

# Create your models here.

class Home(models.Model):
    site_title = models.CharField(max_length=50)
    heading = models.CharField(max_length=100, null=True, blank=True)
    sub_heading = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.heading

class Footer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    privacy_policy = models.CharField(max_length=100, null=True, blank=True)
    terms_conditions = models.CharField(max_length=100, null=True, blank=True)
    faq_help = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class ContactAddress(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='home_gallery', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Newsletter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    paragraph = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)