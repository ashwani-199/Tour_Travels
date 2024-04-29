from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request, 'travel_guides/team.html')