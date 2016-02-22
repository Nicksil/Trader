from django.views.generic import ListView

from eve.models import MarketType
from eve.models import Region
from eve.models import SolarSystem


class MarketTypeListView(ListView):

    model = MarketType


class RegionListView(ListView):

    model = Region


class SolarSystemListView(ListView):

    model = SolarSystem
