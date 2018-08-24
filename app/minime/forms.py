from django import forms


class ShortenURLForm(forms.Form):
    url = forms.URLField(
        required=True,
        label='URL',
        widget=forms.URLInput(attrs={
            'placeholder': 'URL to shorten',
            'autofocus': True,
            'class': 'form-control',
        })
    )
