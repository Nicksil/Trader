from django.conf.urls import url

from finder import views

urlpatterns = [
    url(r'^single-type/$', views.SingleTypeLookupView.as_view(), name='single_type_lookup_view'),
]
