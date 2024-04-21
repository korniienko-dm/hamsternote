from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from note.models import Note
from sharing_notes.models import SharingNote
from .models import Notebook
from .forms import NotebookForm
from .forms import EditNotebookForm


@login_required
def notebook_list(request):
    """
    Render the list of notebooks.
    Displays a list of notebooks created by the current user.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    context = {
        'category': 'notebooks',
        'user_notebooks': user_notebooks,
    }
    return render(request, 'notebook/notebook_list.html', context)


@login_required
def notebook_detail(request, notebook_id):
    """
    Render the detail page for a notebook.
    Displays details of a specific notebook including its associated notes and sharing information.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    shared_notes = SharingNote.objects.filter(
        owner=current_user).order_by('-created_at')
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    shared_count = list()
    for user_note in notes:
        shared_count.append(
            {'note_id': user_note.id, 'shared_count': shared_notes.filter(note=user_note).count()})
    context = {
        'category': 'notebooks',
        'notebook_id': notebook_id,
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notes': notes,
        'shared_notes': shared_notes,
        'shared_count': shared_count,
    }
    return render(request, 'notebook/notebook_detail.html', context)


@login_required
def notebook_create(request):
    """
    Handle notebook creation.
    Allows users to create a new notebook.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)

    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            # Create a new notepad
            new_notebook = form.save(commit=False)
            new_notebook.owner = request.user
            new_notebook.created_by = request.user
            new_notebook.save()
            # Redirect after creating a notepad
            return redirect('notebook_list')
    else:
        form = NotebookForm()
    context = {
        'category': 'notebooks',
        'form': form,
        'user_notebooks': user_notebooks,
    }
    return render(request, 'notebook/notebook_create.html', context)


@login_required
def notebook_edit(request, notebook_id):
    """
    Handle notebook editing.
    Allows users to edit an existing notebook.
    """
    current_user = request.user
    notebook = get_object_or_404(Notebook, id=notebook_id)
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    notes_in_notebooks = Note.objects.filter(notebook=notebook)
    form = EditNotebookForm(instance=notebook)

    if request.method == 'POST':
        form = EditNotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            form.save()
            return redirect('notebook_edit', notebook_id=notebook_id)

    context = {
        'notebook': notebook,
        'notebook_id': notebook_id,
        'form': form,
        'user_notebooks': user_notebooks,
        'notes_in_notebooks': notes_in_notebooks,
    }
    return render(request, 'notebook/notebook_edit.html', context)


@login_required
def notebook_delete(request, notebook_id):
    """
    Handle notebook deletion.
    Allows users to delete an existing notebook.
    """
    notebook = Notebook.objects.get(pk=notebook_id)
    notebook.delete()
    return redirect('notebook_list')
