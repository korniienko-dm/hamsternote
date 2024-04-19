from tasks.forms import TaskForm
from tasks.models import Task
from tasks.tasks import send_email_notification
from django.shortcuts import render
from django.shortcuts import redirect


def tasks_list(request):
    """
    Renders a list of tasks associated with the current user.
    """
    current_user = request.user
    tasks = Task.objects.filter(owner=current_user)
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


def create_task(request):
    """
    Renders a form to create a new task and handles form submission to create the task.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            # Schedule Celery task based on reminder_method
            if task.reminder_method == 'email':
                send_email_notification.apply_async(args=[task.id], eta=task.remind_at)
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})