from django import forms
from users.models import CustomUser

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

        labels = {
            'username': 'Логін',
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'email': "Email",
        }

        help_texts = {
            'username': '',
        }
