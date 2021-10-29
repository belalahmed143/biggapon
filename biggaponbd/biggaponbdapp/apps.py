from django.apps import AppConfig


class BiggaponbdappConfig(AppConfig):
    name = 'biggaponbdapp'

    def ready(self):
        import biggaponbdapp.signals