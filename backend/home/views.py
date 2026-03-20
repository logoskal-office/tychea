from django.shortcuts import render
from services.models import WebDesign

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def portfolio(request):
    return render(request, 'home/portfolio.html')

def components(request):
    designs = WebDesign.objects.reverse()[:8]
    return render(request, 'components.html', {'designs': designs}) 