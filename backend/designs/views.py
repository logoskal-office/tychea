from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, Sector
from django.core.paginator import Paginator
from django.db.models import Q, Count


def designs(request):
    designs = Design.objects.all()
    paginator = Paginator(designs, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'designs/designs.html', {'designs': page_obj})


def designs_list(request):
    """Full designs list page with search, filtering, sorting, and pagination."""
    queryset = Design.objects.filter(public=True)

    # --- Search ---
    query = request.GET.get('q', '').strip()
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )

    # --- Sector Filter ---
    active_sector = request.GET.get('sector', '')
    active_sector_name = ''
    if active_sector:
        try:
            active_sector = int(active_sector)
            queryset = queryset.filter(sectors__id=active_sector)
            sector_obj = Sector.objects.filter(id=active_sector).first()
            if sector_obj:
                active_sector_name = sector_obj.name
        except (ValueError, TypeError):
            active_sector = ''

    # --- Rating Filter ---
    min_rating = request.GET.get('rating', '')
    if min_rating:
        try:
            min_rating = int(min_rating)
            queryset = queryset.filter(rating__gte=min_rating)
        except (ValueError, TypeError):
            min_rating = ''

    # --- Sorting ---
    sort = request.GET.get('sort', '-pinned,-created_at')
    allowed_sorts = {
        'name', '-name', 'rating', '-rating',
        'created_at', '-created_at', '-pinned,-created_at',
    }
    if sort not in allowed_sorts:
        sort = '-pinned,-created_at'
    
    order_fields = sort.split(',')
    queryset = queryset.order_by(*order_fields)

    # Deduplicate (ManyToMany join can cause duplicates)
    queryset = queryset.distinct()

    # Total count before pagination
    total_count = Design.objects.filter(public=True).count()

    # --- Pagination ---
    per_page = 12
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Build smart page range (with ellipsis)
    page_range = _get_page_range(page_obj.number, paginator.num_pages)

    # All sectors for filter chips (with design count)
    sectors = Sector.objects.annotate(
        design_count=Count('designs', filter=Q(designs__public=True))
    ).filter(design_count__gt=0).order_by('name')

    context = {
        'designs': page_obj,
        'query': query,
        'active_sector': active_sector,
        'active_sector_name': active_sector_name,
        'min_rating': min_rating,
        'sort': sort,
        'sectors': sectors,
        'total_count': total_count,
        'star_range': range(1, 6),
        'page_range': page_range,
    }
    return render(request, 'designs/designs-list.html', context)


def _get_page_range(current_page, total_pages, window=2):
    """Generate a smart page range with ellipsis for pagination."""
    if total_pages <= 7:
        return list(range(1, total_pages + 1))
    
    pages = []
    # Always show first page
    pages.append(1)
    
    # Calculate window around current page
    start = max(2, current_page - window)
    end = min(total_pages - 1, current_page + window)
    
    # Add ellipsis after first page if needed
    if start > 2:
        pages.append('...')
    
    # Add pages in window
    for p in range(start, end + 1):
        pages.append(p)
    
    # Add ellipsis before last page if needed
    if end < total_pages - 1:
        pages.append('...')
    
    # Always show last page
    pages.append(total_pages)
    
    return pages


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
