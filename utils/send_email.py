from django.core.mail import send_mail

def send_custom_email(subject, message, from_email, recipient_list, fail_silently=False, **kwargs):
    """
    Send an email with custom parameters.

    Args:
        subject (str): The subject of the email.
        message (str): The content of the email.
        from_email (str): The sender's email address.
        recipient_list (list): A list of recipient email addresses.
        fail_silently (bool, optional): Whether to suppress exceptions (defaults to False).
        **kwargs: Additional keyword arguments for the send_mail function.

    Returns:
        bool: True if the email was successfully sent, False otherwise.
    """
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently, **kwargs)
        return True
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
        return False