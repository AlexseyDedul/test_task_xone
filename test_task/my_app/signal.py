from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile, Category

const_category_list = [
    "Забота о себе",
    "Зарплата",
    "Здоровье и фитнес",
    "Кафе и рестораны",
    "Машина",
    "Образование",
    "Отдых и развлечения",
    "Платежи, комиссии",
    "Покупки: одежда, техника",
    "Продукты",
    "Проезд"
]


def __create_categories(str_category):
    return Category.objects.create(category=str_category)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userProfile = UserProfile.objects.create(user=instance, balance_profile=0.0)
        for item in const_category_list:
            userProfile.category.add(__create_categories(item))

