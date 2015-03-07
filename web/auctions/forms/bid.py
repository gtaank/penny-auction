from django import forms
from django.forms.util import ErrorList


class BidForm(forms.Form):
    bid = forms.Field()

    class Meta:
        fields = ['bid', ]

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None,
                 empty_permitted=False):
        super(BidForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted)
        if initial:
            self.fields['bid'] = forms.FloatField(min_value=initial['bid'], initial=initial['bid'])