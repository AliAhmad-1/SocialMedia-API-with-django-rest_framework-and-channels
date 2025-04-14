import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()



from channels.routing import URLRouter,ProtocolTypeRouter
from app.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
from .middleware import JWTAuthMiddleware

application = ProtocolTypeRouter({
"http":get_asgi_application(),
"websocket":
        JWTAuthMiddleware(URLRouter(websocket_urlpatterns))
    })
