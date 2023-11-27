from fastapi import APIRouter

from backend.auth.controller import register_user
from backend.auth.models import User


router = APIRouter()

@router.post("/register")
async def register(user: User):
    '''
    API Endpoint to Register a User
    '''
    jwt_token = await register_user(user)
    return {"message": "User registered successfully!"}

@router.get("/")
async def home():
    return {"hello"}