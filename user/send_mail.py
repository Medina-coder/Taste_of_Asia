from django.core.mail import send_mail


def send_confirmation_email(user):
    print("ok")
    code = user.activation_code
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    to_email = user.email
    print(to_email)
    send_mail(
        'Activation',
        full_link,
        'kedeikulkyzy.medina@gmail.com',
        [to_email],
        fail_silently=False,
    )

