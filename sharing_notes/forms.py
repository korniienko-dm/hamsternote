from django import forms

from user_contacts.models import Contact
from .models import SharingNote


class SharingNoteForm(forms.ModelForm):
    """
    Form class for creating and updating sharing notes.
    This form allows users to share notes with their contacts and set permissions.
    """
    def __init__(self, *args, user=None, **kwargs):
        """
        Initializes the form instance.
        """
        super().__init__(*args, **kwargs)
        if user is not None:
            # Limit the selection list to only the current user's contacts
            self.fields['shared_with'].queryset = Contact.objects.filter(user=user)

    class Meta:
        """
        Meta class specifying the model and fields for the form.
        """
        model = SharingNote
        fields = ['shared_with', 'can_view', 'can_edit']
        widgets = {
            'shared_with': forms.Select(attrs={'class': 'form-control'}),
            'can_view': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'shared_with': 'Поділитися з контактом',
            'can_view': 'Дозволити перегляд',
            'can_edit': 'Дозволити редагування',
        }
