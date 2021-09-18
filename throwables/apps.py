from django.apps import AppConfig


class ThrowablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'throwables'

    def ready(self):
        import throwables.signals
