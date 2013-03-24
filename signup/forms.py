from django import forms
import signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = signup