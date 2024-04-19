from django import forms
from users.models import CustomUser


class UserSearchForm(forms.Form):
    """
    Form for searching users by email.
    This form allows users to search for other users by email.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Введіть email"

    email = forms.EmailField(label='')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувача з цією електронною адресою не існує.")
        return email
