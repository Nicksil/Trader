from django.views.generic import ListView

from eve.models import MarketType
from eve.models import Region
from eve.models import SolarSystem


class MarketTypeListView(ListView):

    model = MarketType
    template_name = 'explorer/market_type_list.html'


class RegionListView(ListView):

    model = Region
    template_name = 'explorer/region_list.html'


class SolarSystemListView(ListView):

    model = SolarSystem
    template_name = 'explorer/solar_system_list.html'
