from fastapi import HTTPException, status
from backend.auth.auth import sign_tokens
from backend.auth.config import Config
from backend.auth.database import DatabaseUtils
from backend.auth.exceptions import CustomException
from backend.auth.models import LoginUser, User
from backend.auth.schemas import UserModel


async def register_user(user: User):
    '''
    Function to handle user registration
    '''
    try:
        user_exists = await DatabaseUtils.check_for_existing_email(user)
        
        if user_exists:
            raise CustomException.EmailAlreadyTakenException
    
        user_model = await UserModel.create(**user.model_dump())
        
        user_model.generate_password_hash(user_model.password)
        
        await DatabaseUtils.save_user(user_model)
        return sign_tokens(user_model)
    
    except CustomException.DatabaseOperationException as e:
        raise CustomException.DatabaseOperationException(f"Saving user to database failed! Error message = {e}")
    
async def login_user(user_credential: LoginUser):
    '''
    Function to handle user login
    '''
    user = await DatabaseUtils.get_user_by_email(user_credential.email) 
    
    if user and user.verify_password(user_credential.password):
        return user
    else:
        raise CustomException.IncorrectPasswordOrEmailException()

        