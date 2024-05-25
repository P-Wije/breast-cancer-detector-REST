from django.apps import AppConfig


class MainServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_service'

    def ready(self):
        import main_service.signals