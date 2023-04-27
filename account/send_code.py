from django.core.mail import send_mail


def send_activation_code(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Activation code for your Online School account',
        full_link,
        'bekbol.2019@gmail.com',
        [email]
    )
