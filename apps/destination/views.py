from django.shortcuts import render
from . models import * 

def destination(request):
    destination_obj = Destination.objects.get(pk=1)
    destinationCard = DestinationCard.objects.all()

    context = {
        'destination_obj': destination_obj,
        'destinationCard': destinationCard
    }
    return render(request, 'destination.html', context)