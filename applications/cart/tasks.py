import time

from shop.celery import app
from django.core.mail import send_mail

@app.task
def celery_order_mail(email, body):
    full_link = f'Привет, спасибо тебе за заказ\nМы с тобой свяжемся \n{body}'
    send_mail(
        'From shop project',
        full_link,
        'vladislav001015@gmail.com',
        [email]
    )