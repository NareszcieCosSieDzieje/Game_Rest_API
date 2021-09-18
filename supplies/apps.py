from django.apps import AppConfig


class SuppliesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'supplies'

    def ready(self):
        import supplies.signals
