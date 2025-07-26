from django import forms
from .models import CustomUser

class ExampleFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
    
    def validate_password(self, value):
        if len(value) <= 8:
            raise forms.ValidationError("Password cannot be less than 8 digit")
        return value
       