from django.core.mail import EmailMessage


def mass_email_send(subject, body, to):
    email = EmailMessage(
        subject=subject,
        body=body,
        to=to   # []for i in users ...
    )

    email.send()

