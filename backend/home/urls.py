from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='home-page'),
    path('about/', about, name='about-page'),
    path('contact/', contact, name='contact-page'),
]