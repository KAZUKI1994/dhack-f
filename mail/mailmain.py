from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

#READ THIS -->> https://docs.djangoproject.com/en/1.8/topics/emai/
def send_to():
    #sample->
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'

    msg = EmailMultiAlternatives('Subject', text_content, 'shinjimadoshisha@gmail.com', ['send_to@gmail.com','send_to@hoge.com',])

    msg.attach_alternative(html_content, "text/html")

    msg.send()

    #<-sample
