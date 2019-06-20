from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }
        )
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Message'
        }
    ))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "gmail.com" not in email:
            raise forms.ValidationError('Email has to be gmail.com')
        return email


