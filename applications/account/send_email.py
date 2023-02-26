from django.core.mail import send_mail

def send_activateion_code(email, code):
    send_mail(
        'Register on my web_site', #title
        f'Вы хотите зарегистрироваться на моем сайте.Остался всего один шаг-перейти по ссылке.Если это не вы,ты просто проигнорируйте это сообщение. http://localhost:8000/account/activate/{code}', #body
        'assault114@gmail.com', #from
        [email] #to


    )
def send_activation_code2(email, code):
    send_mail(
        'Register on my web_site', #title
        f'Вы хотите забронировать отель на моем сайте.Остался всего один шаг-перейти по ссылке.Если это не вы,ты просто проигнорируйте это сообщение. http://localhost:8000/booking/activate/{code}', #body
        'assault114@gmail.com', #from
        [email] #to


    )


