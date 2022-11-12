import random

from celery.schedules import crontab

from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from my_app.models import UserProfile
from test_task.celery import app

app.conf.beat_schedule = {
    'every': {
        'task': 'send_email_task',
        'schedule': crontab(),
        # 'schedule': crontab(minute=30, hour=6),
    },
}


@shared_task(name='send_email_task')
def send_email_task():
    user_profile = UserProfile.objects.prefetch_related('transaction')
    data = "Hello"
    for user in user_profile:
        transactions = ""
        # for tr in user.transaction:
        #     transactions = transactions + str(tr)
        send_mail(subject='Welcome!', message=str(user.transaction), from_email=EMAIL_HOST_USER,
              recipient_list=[user.user.email, ], fail_silently=False)

