from django.conf.urls import url

from explorer import views

urlpatterns = [
    url(r'^regions/$', views.RegionListView.as_view(), name='region_list_view'),
]
