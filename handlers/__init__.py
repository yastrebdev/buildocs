from .commands import router as commands_router
from .messages import router as messages_router
from .callbacks import router as callbacks_router

routers = [
    callbacks_router,
    commands_router,
    messages_router
]