from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Full name",
                "autocomplete": "name",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email address",
                "autocomplete": "email",
            }
        ),
    )
    phone = forms.CharField(
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Phone number",
                "autocomplete": "tel",
            }
        ),
    )
    subject = forms.CharField(
        max_length=160,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Subject",
            }
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-input form-textarea",
                "placeholder": "Tell us how we can help",
                "rows": 5,
            }
        ),
    )
