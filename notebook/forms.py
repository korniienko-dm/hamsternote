from django import forms
from .models import Notebook


class NotebookForm(forms.ModelForm):
    """
    Form class for creating a new notebook.
    This form allows users to create a new notebook by providing a title.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "Назва нового блокноту"

    class Meta:
        """
        Meta class for the NotebookForm.
        Specifies the model and fields for the form.
        """
        model = Notebook
        fields = ['title']

        labels = {
            'title': '',
        }


class EditNotebookForm(forms.ModelForm):
    """
    Form class for editing an existing notebook.
    This form allows users to edit the title of an existing notebook.
    """
    class Meta:
        """
        Form class for editing an existing notebook.
        This form allows users to edit the title of an existing notebook.
        """
        model = Notebook
        fields = ['title']

        labels = {
            'title': '',
        }
