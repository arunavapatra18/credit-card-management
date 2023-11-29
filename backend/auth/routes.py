from fastapi import APIRouter
from backend.auth.auth import sign_tokens

from backend.auth.controller import login_user, register_user
from backend.auth.models import LoginUser, User


router = APIRouter()

@router.post("/register")
async def register(user: User):
    '''
    API Endpoint to Register a User
    '''
    jwt_token = await register_user(user)
    return {"message": "User registered successfully!"}

@router.post("/login")
async def login(user: LoginUser):
    '''
    API Endpoint to Login a User
    '''
    valid_user = await login_user(user)
    
    if valid_user:
        return sign_tokens(valid_user)
    
@router.get("/")
async def home():
    return {"hello"}