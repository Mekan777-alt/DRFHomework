from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_password_reset_email(user_email, reset_link):
    subject = 'Password Reset'
    message = f'Перейдите по следующей ссылке, чтобы сбросить пароль: {reset_link}'
    from_email = 'mekan.mededov@mail.ru'
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
