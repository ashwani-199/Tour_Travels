from django.shortcuts import render
from . models import *
from apps.about.models import About, AboutFeatures
from apps.service.models import ServiceCard, Services


def index(request):
    about = About.objects.get(pk=1)
    about_cards = AboutFeatures.objects.all()

    services = Services.objects.get(pk=1)
    service_cards = ServiceCard.objects.all()

    context = {
        'about': about,
        'about_cards': about_cards,
        'services': services,
        'service_cards': service_cards
    }
    return render(request, 'helper/index.html', context)



















