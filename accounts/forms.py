from django import forms
from .models import Account

class RegistrationForm(forms.Form):
    class Meta:
        model = Account
        fields=['firs_name', 'last_name', 'phone_number','email','password' ]
        