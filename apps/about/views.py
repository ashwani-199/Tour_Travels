from django.shortcuts import render
from .models import About, AboutFeatures
# Create your views here.

def about(request):
    about_obj = About.objects.get(pk=1)
    about_feature = AboutFeatures.objects.all()

    context = {
        'about': about_obj,
        'about_features': about_feature
    }
    return render(request, 'about.html', context)