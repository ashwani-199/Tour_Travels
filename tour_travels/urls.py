from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.helper.urls')),
    path('about/', include('apps.about.urls')),
    path('services/', include('apps.service.urls')),
    path('packages/', include('apps.package.urls')),
    path('destination/', include('apps.destination.urls')),
    path('booking/', include('apps.booking.urls')),
    path('contact/', include('apps.contact.urls')),
    path('testimonial/', include('apps.testimonial.urls')),
    path('travel_guides/', include('apps.travel_guides.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
