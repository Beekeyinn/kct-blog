from django.core.mail import send_mail
from django.conf import settings


def send_contact_email(message, email, name):
    send_mail(
        subject="Contact message from blog",
        message=message,
        recipient_list=[email],
        from_email=settings.EMAIL_HOST_USER,
    )
