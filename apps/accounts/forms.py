from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(label=_("Email"), max_length=254)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
