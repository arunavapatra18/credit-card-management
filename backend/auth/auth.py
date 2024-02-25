import datetime
import jwt
from fastapi import HTTPException

from backend.auth.config import Config
from backend.auth.schemas import UserModel

def sign_tokens(user: UserModel):
    '''
    Function to sign tokens for the user
    '''
    
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    
def generate_access_token(user: UserModel):
    '''
    Function to generate access tokens for the user
    '''
    
    expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {
        "sub": str(user.id),
        "exp": expiry
    }
    encoded_jwt = jwt.encode(data, Config.JWT_TOKEN, algorithm=Config.JWT_ALGORITHM)
    return encoded_jwt

def generate_refresh_token(user: UserModel):
    '''
    Function to generate refresh token for the user
    '''
    
    expiry = datetime.datetime.utcnow() + datetime.timedelta(days=Config.REFRESH_TOKEN_EXPIRE_DAYS)
    data = {
        "sub": str(user.id),
        "exp": expiry
    }
    encoded_jwt = jwt.encode(data, Config.JWT_TOKEN, algorithm=Config.JWT_ALGORITHM)
    return encoded_jwt

def decode_token(token: str): 
    '''
    Function to decode to the input token
    '''
    
    try:
        decoded_token = jwt.decode(token, Config.JWT_TOKEN, algorithms=[Config.JWT_ALGORITHM])
        return decoded_token["sub"]  
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")