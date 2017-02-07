from django.apps import AppConfig


class GaleryConfig(AppConfig):
    name = 'galery'

    def ready(self):
        import galery.signals
