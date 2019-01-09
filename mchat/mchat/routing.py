from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import nchat.routing

application = ProtocolTypeRouter({
    
    'websocket': AuthMiddlewareStack(
        URLRouter(
            nchat.routing.websocket_urlpatterns
        )
     ),
 })
