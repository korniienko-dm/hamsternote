from datetime import datetime

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'remind_at', 'reminder_method', 'attachment']
        widgets = {
            'remind_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

        initial = {
            'remind_at': datetime.now().strftime('%Y-%m-%dT%H:%M')
        }