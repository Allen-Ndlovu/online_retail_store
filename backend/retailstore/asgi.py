import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import notifications.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retailstore.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(notifications.routing.websocket_urlpatterns),
})
