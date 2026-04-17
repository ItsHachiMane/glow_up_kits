import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glow_up_kits.settings")

application = get_asgi_application()

