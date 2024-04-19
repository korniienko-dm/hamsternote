from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from note.forms import NoteForm, ContentEditForm
from note.models import Note
from notebook.models import Notebook
from user_contacts.models import Contact
from users.models import CustomUser
from .forms import SharingNoteForm
from .models import SharingNote


def shared_note_list(request):
    """
    View function to display the list of shared notes.
    """
    current_user = request.user
    context = {
        'category': 'shared',
    }
    return render(request, 'sharing_notes/shared_note_list.html', context)


def shared_note_for_me(request):
    """
    View function to display shared notes for the current user.
    """
    current_user = request.user
    contacts = Contact.objects.filter(contact_user=current_user)
    contact_users = [contact for contact in contacts]
    shared_notes = SharingNote.objects.filter(shared_with__in=contact_users).order_by('-created_at')

    context = {
        'category': 'shared',
        'subcategory': 'shared_for_me',
        'shared_notes': shared_notes,
    }
    return render(request, 'sharing_notes/shared_note_for_me.html', context)


def shared_note_for_me_detail(request, shared_note_id):
    """
    View function to delete a contact from a shared note.
    """
    current_user = request.user
    note = get_object_or_404(Note, pk=shared_note_id)
    contacts = Contact.objects.filter(contact_user=current_user)
    contact_users = [contact for contact in contacts]
    shared_notes = SharingNote.objects.filter(shared_with__in=contact_users).order_by('-created_at')

    context = {
        'category': 'shared',
        'subcategory': 'shared_for_me',
        'note': note,
        'note_id': shared_note_id,
        'shared_notes': shared_notes,
    }
    return render(request, 'sharing_notes/shared_note_for_me_detail.html', context)


def shared_note_for_me_edit(request, shared_note_id):
    """
    View for editing shared notes intended for the current user.
    """
    current_user = request.user
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    note = get_object_or_404(Note, pk=shared_note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    contacts = Contact.objects.filter(contact_user=current_user)
    contact_users = [contact for contact in contacts]
    shared_notes = SharingNote.objects.filter(shared_with__in=contact_users)

    for shared_note in shared_notes:
        if shared_note_id == shared_note.note.id and shared_note.can_edit == False:
            return redirect(reverse('shared_note_for_me_detail', kwargs={'shared_note_id': shared_note_id}))

    if request.method == 'POST':
        form = ContentEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse('shared_note_for_me_detail', kwargs={'shared_note_id': shared_note_id}))
    else:
        form = ContentEditForm(instance=note)

    context = {
        'category': 'shared',
        'subcategory': 'shared_from_me',
        'shared_notes': shared_notes,
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'form': form,
        'note_id': shared_note_id,
    }
    return render(request, 'sharing_notes/shared_note_for_me_edit.html', context)


def shared_note_from_me(request):
    """
    View for displaying shared notes created by the current user.
    """
    current_user = request.user
    shared_notes = SharingNote.objects.filter(owner=current_user).order_by('-created_at')

    context = {
        'category': 'shared',
        'subcategory': 'shared_from_me',
        'shared_notes': shared_notes,
    }
    return render(request, 'sharing_notes/shared_note_from_me.html', context)


def shared_note_from_me_detail(request, shared_note_id):
    """
    View for displaying details of a shared note created by the current user.
    """
    current_user = request.user
    shared_notes = SharingNote.objects.filter(owner=current_user).order_by('-created_at')
    note = get_object_or_404(Note, pk=shared_note_id)

    context = {
        'category': 'shared',
        'subcategory': 'shared_from_me',
        'shared_notes': shared_notes,
        'note': note,
        'note_id': shared_note_id,
    }
    return render(request, 'sharing_notes/shared_note_from_me_detail.html', context)


def shared_note_from_me_edit(request, shared_note_id):
    """
    View for editing a shared note created by the current user.
    """
    current_user = request.user
    shared_notes = SharingNote.objects.filter(owner=current_user).order_by('-created_at')
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    note = get_object_or_404(Note, pk=shared_note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=current_user)
        if form.is_valid():
            form.save()
            return redirect(reverse('shared_note_from_me_detail', kwargs={'shared_note_id': shared_note_id}))
    else:
        form = NoteForm(instance=note, user=current_user)

    context = {
        'category': 'shared',
        'subcategory': 'shared_from_me',
        'shared_notes': shared_notes,
        'user_notebooks': user_notebooks,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'form': form,
        'note_id': shared_note_id,
    }
    return render(request, 'sharing_notes/shared_note_from_me_edit.html', context)


def shared_note_from_me_settings_change(request, shared_note_id):
    """
    View for changing sharing settings of a shared note created by the current user.
    """
    current_user = request.user
    shared_notes = SharingNote.objects.filter(owner=current_user).order_by('-created_at')
    user_notebooks = Notebook.objects.filter(created_by=current_user)
    note = get_object_or_404(Note, pk=shared_note_id)
    notebook_id = note.notebook.id
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    notes = Note.objects.filter(notebook=notebook).order_by('-updated_at')
    form = SharingNoteForm(request.POST or None, user=current_user)
    note_shared_with_users = SharingNote.objects.filter(
        note=note, owner=request.user)

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
        'category': 'shared',
        'subcategory': 'shared_from_me',
        'shared_notes': shared_notes,
        'notebook': notebook,
        'notebook_id': notebook_id,
        'notes': notes,
        'note': note,
        'note_id': shared_note_id,
        'form': form,
        'note_shared_with_users': note_shared_with_users,
    }
    return render(request, 'sharing_notes/shared_note_from_me_settings_change.html', context)


def change_access_view_rights(request, note_shared_id):
    """
    View for changing view access rights of a shared note.
    """
    if request.method == 'GET':
        sharing_note = get_object_or_404(SharingNote, id=note_shared_id)
        sharing_note.can_view = not sharing_note.can_view
        sharing_note.save()
    return redirect(request.META.get('HTTP_REFERER', ''))


def change_access_edit_rights(request, note_shared_id):
    """
    View for changing edit access rights of a shared note.
    """
    if request.method == 'GET':
        sharing_note = get_object_or_404(SharingNote, id=note_shared_id)
        sharing_note.can_edit = not sharing_note.can_edit
        sharing_note.save()
    return redirect(request.META.get('HTTP_REFERER', ''))


def del_contact_from_shared_note(request, note_shared_id):
    """
    View for deleting a contact from a shared note.
    """
    if request.method == 'GET':
        sharing_note = get_object_or_404(SharingNote, id=note_shared_id)
        sharing_note.delete()
    return redirect(request.META.get('HTTP_REFERER', ''))
