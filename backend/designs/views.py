from django.shortcuts import render, get_object_or_404, redirect
from .models import Design
from django.core.paginator import Paginator

def designs(request):
    designs = Design.objects.all()
    paginator = Paginator(designs, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'designs/designs.html', {'designs': page_obj})

def design_detail(request, slug):
    design = get_object_or_404(Design, slug=slug)
    if design.link:
        return redirect(design.url)
    return render(request, f'designs/list/{slug}/index.html')


def design_detail_subpage(request, slug, page):
    design = get_object_or_404(Design, slug=slug)
    if design.link:
        return redirect(design.url)
    return render(request, f'designs/list/{slug}/{page}.html')
