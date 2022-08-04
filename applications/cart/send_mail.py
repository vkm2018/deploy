from django.core.mail import send_mail


def order_mail(email, body):
    full_link = f'Привет, спасибо тебе за заказ\nМы с тобой свяжемся \n{body}'
    send_mail(
        'From shop project',
        full_link,
        'vladislav001015@gmail.com',
        [email]
    )