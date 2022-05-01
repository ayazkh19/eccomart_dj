from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# this is the first route(path) django server will be directed to
# from here we include the artstore.urls
# so it will look for an 'app' named artstore
# and the server is then directed to urls file of artstore
urlpatterns = [
    path('', include('artstore.urls')),
    path('admin/', admin.site.urls),
]

# adding images url to the list of routes for dynamic images
# MEDIA_URL and MEDIA_ROOT are defined in settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
