from django.urls import path
from .views import home, about, contact, components, portfolio

urlpatterns = [
    path('', home, name='home-page'),
    path('about/', about, name='about-page'),
    path('contact/', contact, name='contact-page'),
    path('portfolio/', portfolio, name='portfolio-page'),
    path('components/', components, name='components-page'),
]