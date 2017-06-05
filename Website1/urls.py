
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^Songs/',include('Songs.urls')),
    url(r'^admin/', admin.site.urls),
]
