
from django.urls import include, path


urlpatterns = [
    path(r'', include('app.minime.urls')),
]
