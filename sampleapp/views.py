from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mahesh.tanpure1210@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'redirect to a new page')