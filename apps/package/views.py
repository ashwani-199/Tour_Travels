from django.shortcuts import render
from .models import * 

def packages(request):
    packages_obj = Package.objects.get(pk=1)
    package_cards = PackageCard.objects.all()

    context = {
        'packages_obj': packages_obj,
        'package_cards': package_cards
    }
    return render(request, 'package.html', context)
