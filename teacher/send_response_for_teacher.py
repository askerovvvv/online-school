from django.core.mail import send_mail


def response_if_agreed(email):
    send_mail(
        "Online School",
        'We went through your teacher application, right now you have "teacher permission" you can add materials',
        'bekbol.2019@gmail.com',
        [email]
    )


def response_if_deleted(email):
    send_mail(
        "Online School",
        'you are no longer a teacher on our platform',
        'bekbol.2019@gmail.com',
        [email],
    )
