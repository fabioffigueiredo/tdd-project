from fastapi import FastAPI
from store.core.config import settings
from store.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_NAME,
            version="0.0.1",
            root_path=settings.ROOT_PATH,
        )


app = App()
app.include_router(api_router)
