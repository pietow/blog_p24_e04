# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    # username = forms.CharField(max_length=30, label='Username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Custom form initialized")
        self.fields['username'] = forms.CharField(max_length=30, label='Username')

    def save(self, request):
        user = super().save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user

