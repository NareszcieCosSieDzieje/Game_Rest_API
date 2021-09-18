from django.apps import AppConfig


class MapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maps'

    def ready(self):
        import maps.signals
