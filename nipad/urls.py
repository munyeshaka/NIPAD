
from django.contrib import admin
from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^adminanipad/', admin.site.urls),
    re_path(r'^', include('nipadapp.urls')),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)