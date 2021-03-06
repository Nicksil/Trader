from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='site_index'),
    url(r'^explorer/', include('explorer.urls', namespace='explorer')),
    url(r'^finder/', include('finder.urls', namespace='finder')),
    url(r'^admin/', admin.site.urls),
]
