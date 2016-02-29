from django.conf.urls import url

from finder import views

urlpatterns = [
    url(r'^inter-region/$', views.InterRegionLookupView.as_view(), name='inter_region_lookup_view'),
    url(r'^single-type/$', views.SingleTypeLookupView.as_view(), name='single_type_lookup_view'),
]
