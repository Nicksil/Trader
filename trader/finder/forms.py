from django import forms

from eve.models import Region


class SingleTypeLookupForm(forms.Form):

    BUY_OR_SELL = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    region = forms.CharField(label='Region', max_length=256)
    type_name = forms.CharField(label='Market Type', max_length=256)
    buy_or_sell = forms.ChoiceField(widget=forms.RadioSelect, choices=BUY_OR_SELL)


class InterRegionLookupForm(forms.Form):

    regions = Region.objects.all()
    r = []

    for reg in regions:
        r.append((reg.id, reg.name))

    REGIONS = r

    origin = forms.ChoiceField(choices=REGIONS)
    dest = forms.ChoiceField(choices=REGIONS)
    market_group = forms.IntegerField()
