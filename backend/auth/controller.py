from backend.auth.auth import sign_tokens
from backend.auth.config import Config
from backend.auth.database import DatabaseUtils
from backend.auth.exceptions import EmailAlreadyTakenException, DatabaseOperationException
from backend.auth.models import User
from backend.auth.schemas import UserModel


async def register_user(user: User):
    '''
    Function to handle user registration
    '''
    try:
        user_exists = await DatabaseUtils.check_for_existing_email(user)
        
        if user_exists:
            raise EmailAlreadyTakenException()
    
        user_model = await UserModel.create(**user.model_dump())
        
        user_model.generate_password_hash(user_model.password)
        
        await DatabaseUtils.save_user(user_model)
        return sign_tokens(user_model)
    
    except DatabaseOperationException as database_exception:
        raise DatabaseOperationException(f"Saving user to database failed! Error message = {database_exception}")
    
    
    
        