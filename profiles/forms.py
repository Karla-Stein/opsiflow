from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder, remove auto-generated
        labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
