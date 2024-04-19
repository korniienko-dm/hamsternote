from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .models import Contact
from .forms import UserSearchForm


def add_contact(request):
    """
    This view handles the addition of a new contact. If the request method is POST
    and the form is valid, the contact is added to the user's contacts list. If the
    request method is GET, a blank form is displayed to the user.
    """
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            Contact.objects.get_or_create(user=request.user, contact_user=user)
            return redirect('contacts_list')
    else:
        form = UserSearchForm()

    context = {
        'category': 'contacts',
        'form': form,
    }
    return render(request, 'user_contacts/add_contact.html', context)


@login_required
def contacts_list(request):
    """
    View function to display a list of contacts for the current user.
    This view retrieves all contacts associated with the current user and renders
    them in a template.
    """
    contacts = Contact.objects.filter(user=request.user)
    context = {
        'category': 'contacts',
        'contacts': contacts,
    }
    return render(request, 'user_contacts/contacts_list.html', context)


@login_required
def contact_detail(request, contact_id):
    """
    View function to display details of a specific contact.
    This view retrieves details of a specific contact based on the provided contact ID
    and renders them in a template.
    """
    contacts = Contact.objects.filter(user=request.user)
    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        'category': 'contacts',
        'contacts': contacts,
        'select_contact': contact,
    }
    return render(request, 'user_contacts/contact_detail.html', context)


@login_required
def remove_contact(request, contact_id):
    """
    View function to remove a contact.

    This view removes a contact associated with the current user based on the provided
    contact ID.
    """
    contact = Contact.objects.get(id=contact_id)
    if contact.user == request.user:
        contact.delete()
    return redirect('contacts_list')
