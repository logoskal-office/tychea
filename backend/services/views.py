from django.shortcuts import render, redirect
from django.http import Http404
from .models import WebDesign, WebFeature

def services(request):
    return render(request, 'services/services.html')

def web_development(request):
    designs = WebDesign.objects.order_by('?').reverse()
    features = WebFeature.objects.order_by('id').reverse()

    return render(request, 'services/web/web-development.html', {'designs':designs, 'features':features})

def web_designs(request):
    designs = WebDesign.objects.order_by('id').reverse()
    features = WebFeature.objects.order_by('id').reverse()
    return render(request, 'services/web/web-designs.html', {'designs':designs})

def web_design(request, design, page='index'):
    try:
        return render(request, f"services/web/designs/{design}/{page}.html", {'design':design})
    except:
        raise Http404("Design page not found")

def web_design_redirect(request, design):
    return redirect('web-design-page', design, 'index')
