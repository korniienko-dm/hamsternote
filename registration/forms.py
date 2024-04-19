from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomLoginForm(AuthenticationForm):
    """
    We're using the standard Django LoginView, which doesn't provide an easy way to change
    form field attributes directly in the template. However, you can create your own form class based
    on the AuthenticationForm, and then use it in the LoginView.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removing field labels
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        # Set placeholder for fields
        self.fields['username'].widget.attrs.update({'placeholder': 'Логін'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль'})


class CustomUserCreationForm(UserCreationForm):
    """
    This form extends the UserCreationForm provided by Django to include custom validation for the username, email, 
    and password fields. It overrides the clean_email, clean_username, and clean_password methods to perform 
    custom validation logic. It also provides custom error messages for various validation errors.
    """
    error_messages = {
        'username_exists': 'Помилка: Користувач із таким ім\'ям вже існує.',
        'email_exists': 'Помилка: Користувач із такою адресою електронної пошти вже існує.',
        'password_mismatch': 'Помилка: Паролі не співпадають.',
        'password_too_short': 'Помилка: Пароль надто короткий.',
        'password_numeric': 'Помилка: Пароль має містити хоча б одну цифру.',
        'password_lowercase': 'Помилка: Пароль повинен містити хоча б одну малу літеру.',
        'password_uppercase': 'Помилка: Пароль повинен містити хоча б одну велику літеру.',
        'password_more_128_char': 'Помилка: Пароль повинен містити не більше 128 символів.',
        'password_common': 'Помилка: Пароль надто поширений.',
        'invalid': 'Помилка вводу логіну',
    }

    def add_error(self, field, error):
        """Add a custom error message for a specific field."""
        if field == 'username' and 'invalid' in error:
            error = forms.ValidationError(
                self.error_messages['invalid'], code='invalid')
        elif field == 'email' and 'email_exists' in error:
            error = forms.ValidationError(
                self.error_messages['email_exists'], code='email_exists')

        super().add_error(field, error)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removing the autofocus attribute for the input html field
        self.fields['username'].widget.attrs.pop('autofocus', None)
        # Removing field labels
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        # Set placeholder for fields
        self.fields['username'].widget.attrs.update({'placeholder': 'Логін'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Підтвердження пароля'})
        # Set custom help texts
        self.fields['username'].help_text = 'Логін може бути не більше 150 символів. Лише літери, цифри та @/./+/-/_'
        self.fields['email'].help_text = 'Вкажіть вашу актуальну електронну адресу'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = 'Для підтвердження введіть той самий пароль, що й раніше.'

    class Meta:
        """
        Metadata for the CustomUserCreationForm class.
        Specifies the model and fields for the form.
        """
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        """Check if the email address already exists in the database."""
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'], code='email_exists')
        return email

    def clean_username(self):
        """Validate the username field."""
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['username_exists'], code='username_exists')
        if '111' in username:
            raise forms.ValidationError(
                self.error_messages['invalid'], code='invalid')
        return username

    def clean_password(self):
        """Validate the password field."""
        password = self.cleaned_data['password']
        if len(str(password)) > 128:
            raise forms.ValidationError(
                self.error_messages['password_more_128_char'], code='username_exists')
        return password


class CustomUserChangeForm(UserChangeForm):
    """
    A form used for changing user account details.
    This form allows users to change their username and email address.
    """
    class Meta:
        """
        Metadata for the CustomUserChangeForm class.
        Specifies the model and fields for the form.
        """
        model = CustomUser
        fields = ('username', 'email')
