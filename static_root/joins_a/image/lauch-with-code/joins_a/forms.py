from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
    """ the Join form to be displayed when registration """
    class Meta:
        model = Join
        fields = ("first_name", "email_address")
