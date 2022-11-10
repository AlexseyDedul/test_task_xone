from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'

    def ready(self):
        from my_app import signal