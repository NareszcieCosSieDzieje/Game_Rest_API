from django.apps import AppConfig


class AmmunitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ammunition'

    def ready(self):
        import ammunition.signals
