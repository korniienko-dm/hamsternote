from django import forms
from .models import Note
from notebook.models import Notebook
from django_ckeditor_5.widgets import CKEditor5Widget


class NoteForm(forms.ModelForm):
    """
    This form is used to create or update a Note object. It includes fields for 'title', 'content', 'favorite', and
    'notebook'. The 'content' field is rendered using CKEditor5Widget for rich text editing. The form can be initialized
    with an optional 'user' parameter to filter the available 'notebook' choices based on the user's ownership.
    """
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False
        self.fields["title"].widget.attrs["placeholder"] = "Заголовок"
        if user is not None:
            self.fields["notebook"].queryset = Notebook.objects.filter(
                owner=user)

    class Meta:
        model = Note
        fields = ['title', 'content', 'favorite', 'notebook', ]
        widgets = {
            'content': CKEditor5Widget(config_name='extends')
        }

        labels = {
            'title': '',
            'favorite': 'Закріпити замітку: ',
            'content': '',
            'notebook': "Належить до блокноту: ",
        }


class ContentEditForm(forms.ModelForm):
    """
    This form is used to edit the 'content' field of a Note object. It includes a disabled 'title' field and a 'content'
    field rendered using CKEditor5Widget for rich text editing.
    """
    title = forms.CharField(disabled=True)

    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': CKEditor5Widget(config_name='extends')
        }

        labels = {
            'title': '',
            'content': '',
        }
