from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]