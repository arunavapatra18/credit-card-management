from fastapi import Header
from pydantic import UUID4
from tortoise import exceptions as TortoiseException
from tortoise.queryset import Q
from backend.auth.auth import decode_token
from backend.exceptions import CustomException
from backend.auth.models import User
from backend.auth.schemas import UserModel
from tortoise.contrib.pydantic import pydantic_model_creator
    
user_model_pydantic = pydantic_model_creator(UserModel)   

class AuthDatabaseUtils:
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
        
    async def get_user_by_id(id: UUID4):
        try:
            return await UserModel.get(Q(id = id))
        except TortoiseException.DoesNotExist:
            raise CustomException.UserNotfoundException
        
def get_current_user(token: str = Header(...)):
    try:
        user_id = decode_token(token)
        return user_id
    except TortoiseException.DoesNotExist:
        raise CustomException.UserNotfoundException