from django.shortcuts import render
from .models import *


def services(request):
    service_obj = Services.objects.get(pk=1)
    service_card = ServiceCard.objects.all()

    context = {
        'service_obj': service_obj,
        'service_card': service_card
    }
    return render(request, 'service/service.html', context)