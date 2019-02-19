# from celery import task
import django
from django.core.mail import send_mail
from config.config import *
from django.conf import settings
import threading



# @task(name='blog_user.tasks.send_user_mail')
# def send_user_mail(user_email):
#     user_list = [user_email]
#     send_mail(SEND_TITLE,SEND_MESSAGE,settings.EMAIL_FROM,user_list,SEND_HTML_MESSAGE)
#
# @task(name='blog_user.tasks.send_num')
# def send_num(user_email,ran_num):
#     user_list = [user_email]
#     send_message = ran_num
#     send_mail(SEND_TITLE,send_message, settings.EMAIL_FROM, user_list, SEND_HTML_MESSAGE)


class SendUserMailThread(threading.Thread):

    def __init__(self,user_email):
        self.user_email = user_email
        super(SendUserMailThread, self).__init__()
    def run():
        send_mail(SEND_TITLE, SEND_MESSAGE, settings.EMAIL_FROM,self.user_email, SEND_HTML_MESSAGE)

class SendNumThread(threading.Thread):

    def __init__(self,user_email,ran_num):
        self.user_list = [user_email]
        self.ran_num = ran_num
        super(SendNumThread, self).__init__()

    def run(self):
        self.send_message = self.ran_num
        send_mail(SEND_TITLE,self.send_message,settings.EMAIL_FROM,self.user_list,SEND_HTML_MESSAGE)