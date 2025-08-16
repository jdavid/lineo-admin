import importlib

from django.apps import AppConfig
from django.conf import settings

from . import registry


class LineoAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lineo_admin'

    def ready(self):
        # Automatically discover and register sidebar items
        for app in settings.INSTALLED_APPS:
            try:
                mod = importlib.import_module(f"{app}.lineo_admin")
            except ImportError:
                continue

            # Call the registration function with our registry, if available
            register = getattr(mod, 'register', None)
            if register is not None:
                register(registry)
