from django.shortcuts import render
from django.shortcuts import redirect
from .forms import EditProfileForm

def edit_profile(request):
    user = request.user
    form = EditProfileForm(instance=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')

    context = {
        'form': form,
    }

    return render(request, 'user_profile/edit_profile.html', context)
