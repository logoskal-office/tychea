from django.urls import path
from .views import *

urlpatterns = [
    path('', services, name='services-page'),
    path('web/', web_development, name='web-development-page'),
    path('web-designs/', web_designs, name='web-designs-page'),
    path('web-designs/<str:design>/<str:page>/', web_design, name='web-design-page'),
    path('web-designs/<str:design>/', web_design_redirect, name='web-design-redirect'),
]