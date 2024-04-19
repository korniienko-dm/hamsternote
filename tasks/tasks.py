from celery import shared_task
from django.core.mail import send_mail
from .models import Task
from utils.send_email import send_custom_email

@shared_task
def send_email_notification(task_id):
    task = Task.objects.get(pk=task_id)
    # Sending an email notification to the user
    subject = "Test Email"
    message = "This is a test email sent using the send_custom_email function."
    from_email = "hamsternote.mail@gmail.com"
    recipient_list = ["korolev3245137@gmail.com", ]

    # Отправка письма
    if send_custom_email(subject, message, from_email, recipient_list):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")

