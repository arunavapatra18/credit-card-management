from fastapi import FastAPI
from tortoise import Tortoise
from backend.auth.config import Config

from backend.auth import schemas as auth_schemas
from backend.cards import schemas as card_schemas

from backend.auth.routes import auth_router
from backend.cards.routes import cards_router

async def db_init():
    '''
    Initializes mySQL database
    '''
    print("Connecting to MySQL DB...")
    await Tortoise.init(
        db_url=Config.DATABASE_URI,
        modules={
            "models": [auth_schemas, card_schemas]
            }
    )
    print(Tortoise.apps)
    print("Generating schema...")
    await Tortoise.generate_schemas()
    
    print("Connection established!")
    
async def db_close():
    '''
    Close db connection
    '''
    await Tortoise.close_connections()
    print("Connection closed!")

def create_app():
    app = FastAPI()
    app.include_router(auth_router)
    app.include_router(cards_router)
    
    async def startup_event():
        await db_init()
        
    async def shutdown_event():
        await db_close()
        
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)
    
    return app