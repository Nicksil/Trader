from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

import requests

from eve.models import MarketType
from eve.models import Region

from finder.forms import InterRegionLookupForm
from finder.forms import SingleTypeLookupForm

CREST_ORDER_URL = 'https://public-crest.eveonline.com/market/{region_id}/orders/{buy_or_sell}/?type=https://public-crest.eveonline.com/types/{type_id}/'


class SingleTypeLookupView(FormView):

    form_class = SingleTypeLookupForm
    template_name = 'finder/single_type_lookup_form.html'
    success_url = reverse_lazy('finder:single_type_lookup_view')

    def form_valid(self, form):
        region = form.cleaned_data['region']
        type_name = form.cleaned_data['type_name']
        buy_or_sell = form.cleaned_data['buy_or_sell']

        region_obj = Region.objects.get(name__iexact=region)
        type_obj = MarketType.objects.get(name__iexact=type_name)

        region_id = region_obj.id
        type_id = type_obj.id

        url = CREST_ORDER_URL.format(region_id=region_id, buy_or_sell=buy_or_sell, type_id=type_id)

        return super(SingleTypeLookupView, self).form_valid(form)


class InterRegionLookupView(FormView):

    form_class = InterRegionLookupForm
    template_name = 'finder/inter_region_lookup_form.html'
    success_url = reverse_lazy('finder:inter_region_lookup_view')

    def __init__(self, **kwargs):
        self.crest_data = {
            'origin': [],
        }
        super(InterRegionLookupView, self).__init__(**kwargs)

    def form_valid(self, form):

        origin_id = int(form.cleaned_data['origin'])
        dest_id = int(form.cleaned_data['origin'])
        market_group = form.cleaned_data['market_group']

        market_types = MarketType.objects.filter(market_group=market_group)

        for t in market_types:
            url = CREST_ORDER_URL.format(region_id=origin_id, buy_or_sell='sell', type_id=t.id)
            r = requests.get(url)
            r_json = r.json()

            for order in r_json['items']:
                _ = {
                    'price': order['price'],
                    'volume': order['volume'],
                    'station': order['location']['name'],
                    'type_name': order['type']['name'],
                }
                self.crest_data['origin'].append(_)

        return super(InterRegionLookupView, self).form_valid(form)
