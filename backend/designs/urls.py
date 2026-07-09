from designs.views import *
from django.urls import path
from .views import * 

urlpatterns = [
    path('', designs, name='designs-page'),
    path('list/', designs_list, name='design-list-page'),
    path('<str:slug>/', design_detail, name='design-detail-page'),
    path('<str:slug>/<str:page>/', design_detail_subpage, name='design-detail-subpage'),
]
