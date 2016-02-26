from django.conf.urls import url

from explorer import views

urlpatterns = [
    url(r'^markettypes/$', views.MarketTypeListView.as_view(), name='market_type_list_view'),
    url(r'^regions/$', views.RegionListView.as_view(), name='region_list_view'),
    url(r'^solarsystems/$', views.SolarSystemListView.as_view(), name='solar_system_list_view'),
]
