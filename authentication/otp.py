import datetime
from django.contrib.auth import get_user_model
from threading import Thread
from time import sleep
from random import randint
from kavenegar import *
from django.conf import settings
api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
def send_otp_thread(user):
    # send otp to user
    try :
        params = {
            "receptor": user.mobile,
            "token" : user.otp,
            "template":454
        }
        api.verify_lookup(params)
    except :
        pass
    sleep(120)
    if user.is_active :
        user.otp = None
        user.save()
def send_otp(user):
    task = Thread(target=send_otp_thread,args=[user])
    task.start()