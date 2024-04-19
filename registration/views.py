from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib import messages


class CustomLoginView(LoginView):
    """
    A custom login view.
    This view extends the LoginView provided by Django to use a custom login form.
    """
    form_class = CustomLoginForm


class SignUpView(CreateView):
    """
    A view for user registration.
    This view allows users to sign up by providing their username, email, and password.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        """
        Process a valid form submission.
        Save the form if the data is valid and display a success message.
        """
        # Save the form if the data is valid
        response = super().form_valid(form)
        # Adding a message about successful registration
        messages.success(
            self.request, 'Ви успішно зареєстровані! Для входу введіть ваші данні в форму.')
        return response

    def form_invalid(self, form):
        """
        Process an invalid form submission.
        Display error messages to the user.
        """
        # Search for unique error text
        unique_error = next(iter(form.errors.values()), None)
        if unique_error:
            messages.error(self.request, unique_error[0])
        else:
            messages.error(self.request, 'Помилка: Перевірте введені дані.')
        return super().form_invalid(form)
