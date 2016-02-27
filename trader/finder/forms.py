from django import forms


class SingleTypeLookupForm(forms.Form):

    region = forms.CharField(label='Region', max_length=256)
    type_name = forms.CharField(label='Market Type', max_length=256)
