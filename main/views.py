from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from notebook.models import Notebook
from note.models import Note


@login_required
def main_page(request):
    """
    View function to redirect users to the homepage.
    """
    return redirect('homepage')

@login_required
def homepage(request):
    """
    View function to render the main homepage.
    Retrieves notebooks and notes associated with the current user and renders them on the homepage.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    user_notes = Note.objects.filter(notebook__in=user_notebooks)
    context = {
        'user_notebooks': user_notebooks,
        'user_notes': user_notes,
    }
    return render(request, 'main/home_page.html', context)
