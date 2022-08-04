import time

from django.core.mail import send_mail

from applications.spam.models import Contact
from shop.celery import app


@app.task
def celery_send_confirmation_email(code, email):

    time.sleep(10)
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'From shop project',
        full_link,
        'vladislav001015@gmail.com',
        [email]
    )


@app.task
def spam_email(email):

        full_link = f'Hello'
        send_mail(
            'From shop project',
            full_link,
            'vladislav001015@gmail.com',
            [email]
    )