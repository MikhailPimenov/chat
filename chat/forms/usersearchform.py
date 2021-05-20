from django.contrib.auth.models import User
from django import forms


class UserSearchForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]
