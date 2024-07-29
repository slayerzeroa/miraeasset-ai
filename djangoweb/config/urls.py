from django.contrib import admin
from django.urls import path, include
from config.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='main'),
    path('main/', home),
    path('summary/', include('summary.urls'), name='summary'),
    path("admin/", admin.site.urls, name='admin'),
    path("matching/", include("matching.urls"), name='matching'),
    path("community/", include("community.urls"), name='community'),
    path("pbreport/", include("mypage.urls"), name='pbreport'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
