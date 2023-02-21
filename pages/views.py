from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    # to fetch data in front end
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/home.html', data)

def about(request):

    teams = Team.objects.all()
    data = {
        'teams':teams,
    }

    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')