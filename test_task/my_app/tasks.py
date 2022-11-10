import random

from celery.schedules import crontab

from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from my_app.models import UserProfile
from test_task.celery import app

# app.conf.beat_schedule = {
#     'every': {
#         'task': 'send_email_task',
#         'schedule': crontab(),
#         # 'schedule': crontab(minute=30, hour=6),
#     },
# }

schedule_one_day, _ = CrontabSchedule.objects.get_or_create()

try:
    PeriodicTask.objects.create(
        crontab=schedule_one_day,
        name='send_email_task',
        task='send_email_task',
    )
except:
    pass


@shared_task(name='send_email_task')
def send_email_task():
    # user_profile = UserProfile.objects.all()
    data = "Hello"
    # for user in user_profile:
        # recipient_list = [user.email]
    send_mail(subject='Welcome!', message='', from_email=EMAIL_HOST_USER, html_message=data,
              recipient_list=['dedyul@gmail.com'], fail_silently=False)

