from tortoise import Tortoise

from backend.auth.config import Config
from backend.auth.models import User
from backend.auth.schemas import UserModel

async def db_init():
    '''
    Initializes mySQL database
    '''
    print("Connecting to MySQL DB...")
    await Tortoise.init(
        db_url=Config.DATABASE_URI,
        modules={
            "models": ["backend.auth.schemas"]
            }
    )
    
    print("Generating schema...")
    await Tortoise.generate_schemas()
    
    print("Connection established!")
    
async def db_close():
    '''
    Close db connection
    '''
    await Tortoise.close_connections()
    print("Connection closed!")
    
class DatabaseUtils:
    async def save_user(user: UserModel):
        '''
        Save the Tortoise ORM User Model to DB
        '''
        await user.save()
    
    async def check_for_existing_email(user: User):
        '''
        Checks whether user with email exists
        '''
        return await UserModel.exists(email=user.email)

        