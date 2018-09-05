from django import forms


class ShortenURLForm(forms.Form):
    """
    Form for index view
    """
    url = forms.URLField(
        required=True,
        label='URL',
        widget=forms.URLInput(attrs={
            'placeholder': 'URL to shorten',
            'autofocus': True,
            'class': 'form-control',
        })
    )

    password = forms.CharField(
        required=False,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Set a password',
            'class': 'form-control',
        })
    )


class AdminForm(forms.Form):
    """
    Form for admin login view
    """
    hash = forms.SlugField(
        required=True,
        label='hash',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True
        })
    )

    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'autofocus': True,
            'class': 'form-control',
        })
    )
