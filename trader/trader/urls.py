from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^explorer/', include('explorer.urls', namespace='explorer')),
    url(r'^admin/', admin.site.urls),
]
