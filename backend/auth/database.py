from tortoise import Tortoise
from tortoise import exceptions as TortoiseException
from tortoise.queryset import Q

from backend.auth.config import Config
from backend.auth.exceptions import CustomException
from backend.auth.models import LoginUser, User
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
    
    async def get_user_by_email(user_email: str):
        '''
        Gets a user by email
        '''
        try:
            return await UserModel.get(Q(email = user_email))
            
        except TortoiseException.DoesNotExist:
            raise CustomException.UserNotfoundException
        
    async def get_current_user()
        