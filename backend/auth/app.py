from fastapi import FastAPI

from backend.auth.database import db_close, db_init
from backend.auth.routes import router

def create_auth_app():
    app = FastAPI()
    app.include_router(router)
    
    async def startup_event():
        await db_init()
        
    async def shutdown_event():
        await db_close()
        
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)
    
    return app
