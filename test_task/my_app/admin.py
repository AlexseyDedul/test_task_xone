from django.contrib import admin

from .models import Transaction, UserProfile, Category

# Register your models here.

admin.site.register(Transaction)
admin.site.register(UserProfile)
admin.site.register(Category)
