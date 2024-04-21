from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from sharing_notes.models import SharingNote
from users.models import CustomUser
from .models import Note
from .models import Notebook
from .forms import NoteForm
from sharing_notes.forms import SharingNoteForm

@login_required
def note_create(request, notebook_id):
    """
    This view allows a user to create a new note within a specific notebook. It retrieves the current user's notebooks,
    shared notes, and the selected notebook based on the provided notebook ID. If the request method is POST, it
    processes the submitted form data. If the form is valid, it saves the new note and redirects to the note detail
    page. If the method is GET, it renders the note creation form.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    shared_notes = SharingNote.objects.filter(
        owner=current_user).order_by('-created_at')
    notebook = Notebook.objects.get(pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    shared_count = list()
    for user_note in notes:
        shared_count.append(
            {'note_id': user_note.id, 'shared_count': shared_notes.filter(note=user_note).count()})

    if request.method == 'POST':
        form = NoteForm(request.POST, user=current_user)
        if form.is_valid():
            note = form.save(commit=False)
            note.notebook = notebook
            note.author = request.user
            note.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(initial={'notebook': notebook}, user=current_user)
    context = {
        'category': 'notebooks',
        'form': form,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'user_notebooks': user_notebooks,
        'notes': notes,
        'shared_count': shared_count,
    }
    return render(request, 'note/note_create.html', context)


@login_required
def note_detail(request, note_id):
    """
    This view retrieves the current user's notebooks, shared notes, and the selected note based on the provided note
    ID. It renders the note detail page with information about the note, including its content, notebook, and shared
    status.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    shared_notes = SharingNote.objects.filter(
        owner=current_user).order_by('-created_at')
    note = get_object_or_404(Note, pk=note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    shared_count = list()
    for user_note in notes:
        shared_count.append(
            {'note_id': user_note.id, 'shared_count': shared_notes.filter(note=user_note).count()})

    context = {
        'category': 'notebooks',
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'note': note,
        'note_id': note_id,
        'shared_count': shared_count,
    }
    return render(request, 'note/note_detail.html', context)


@login_required
def shared_info_note(request, note_id):
    """
    This view allows a user to share a note with other users. It retrieves the current user's notebooks, shared notes,
    the selected note, and the users with whom the note is shared. If the request method is POST, it processes the
    submitted form data. If the form is valid, it saves the shared note and redirects to the same page. If the method
    is GET, it renders the page with the form to share the note.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    shared_notes = SharingNote.objects.filter(
        owner=current_user).order_by('-created_at')
    note = get_object_or_404(Note, pk=note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    form = SharingNoteForm(request.POST or None, user=current_user)
    note_shared_with_users = SharingNote.objects.filter(
        note=note, owner=request.user)
    shared_count = list()
    for user_note in notes:
        shared_count.append(
            {'note_id': user_note.id, 'shared_count': shared_notes.filter(note=user_note).count()})

    if request.method == 'POST' and form.is_valid():
        shared_note = form.save(commit=False)
        shared_note.owner = request.user
        shared_note.note = note
        shared_with = form.cleaned_data.get("shared_with")
        if SharingNote.objects.filter(note=note, shared_with=shared_with).exists():
            messages.info(
                request, "Ви вже поділилися цим записом з обраним контактом")
        else:
            shared_note.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'category': 'notebooks',
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'note': note,
        'note_id': note_id,
        'form': form,
        'note_shared_with_users': note_shared_with_users,
        'shared_count': shared_count,
    }

    return render(request, 'note/note_shared_info.html', context)


@login_required
def note_edit(request, note_id):
    """
    This view allows a user to edit an existing note. It retrieves the current user's notebooks, shared notes, the
    selected note, and the note to edit based on the provided note ID. If the request method is POST, it processes the
    submitted form data. If the form is valid, it saves the edited note and redirects to the note detail page. If the
    method is GET, it renders the form with the current note data.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    shared_notes = SharingNote.objects.filter(
        owner=current_user).order_by('-created_at')
    note = get_object_or_404(Note, pk=note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    note_select = Note.objects.filter(id=note_id).first()
    shared_count = list()
    for user_note in notes:
        shared_count.append(
            {'note_id': user_note.id, 'shared_count': shared_notes.filter(note=user_note).count()})

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=current_user)
        if form.is_valid():
            form.save()
            return redirect(reverse('note_detail', kwargs={'note_id': note_id}))
    else:
        form = NoteForm(instance=note, user=current_user)

    context = {
        'category': 'notebooks',
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'form': form,
        'note_id': note_id,
        'note_select': note_select,
        'shared_count': shared_count,
    }
    return render(request, 'note/note_edit.html', context)


@login_required
def note_delete(request, note_id):
    """
    This view allows a user to delete an existing note. It retrieves the note to delete based on the provided note ID,
    deletes the note, and redirects to the detail page of the notebook to which the note belonged.
    """
    note = Note.objects.get(pk=note_id)
    notebook_id = note.notebook.id
    note.delete()
    return redirect('notebook_detail', notebook_id=notebook_id)


@login_required
def note_delete_from_favorite(request, note_id):
    """
    This view allows a user to remove a note from their favorites list. It retrieves the note based on the provided
    note ID, updates the note's favorite status to False, and redirects to the previous page.
    """
    note = Note.objects.get(pk=note_id)
    note.favorite = False
    note.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def note_add_favorite(request, note_id):
    """
    This view allows a user to add a note to their favorites list. It retrieves the note based on the provided note ID,
    updates the note's favorite status to True, and redirects to the previous page.
    """
    note = Note.objects.get(pk=note_id)
    note.favorite = True
    note.save()
    return redirect(request.META.get('HTTP_REFERER'))
