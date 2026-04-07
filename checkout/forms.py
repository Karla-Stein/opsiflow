from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_first_name',
                  'user_last_name',
                  'user_email',
                  'user_phone',
                  'billing_address_1',
                  'billing_address_2',
                  'billing_county',
                  'billing_city',
                  'billing_postalcode',
                  'billing_country')

    def __init__(self, *args, **kwargs):
        """
        Add placeholder, remove auto-generated
        labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_first_name': 'First Name',
            'user_last_name': 'Last Name',
            'user_email': 'Email Address',
            'user_phone': 'Phone Number',
            'billing_address_1': 'Street Address 1',
            'billing_address_2': 'Street Address 2',
            'billing_county': 'County',
            'billing_city': 'City',
            'billing_postalcode': 'Postal Code',
            'county': 'County, State or Locality',
        }

        self.fields['user_first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'billing_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
