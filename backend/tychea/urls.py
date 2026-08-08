from django.urls import re_path
from django.views.static import serve
from django.urls import re_path
from designs.views import linker_view_subpage
from designs.views import linker_view
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sites/<uuid:uid>/', linker_view, name='linker-page'),
    path('sites/<uuid:uid>/<str:page>/', linker_view_subpage, name='linker-subpage'),
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    # path('designs/', include('designs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]