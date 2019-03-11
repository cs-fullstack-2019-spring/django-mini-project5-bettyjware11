from django import forms
from .models import RecipeModel, UserModel
from datetime import date

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ["foreignKeyToUser"]



class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords DO NOT MATCH!!!!!!!!!!!!!")




