from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path(r'', include('app.minime.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
