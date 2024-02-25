import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/arunava/Documents/credit-card-management/.env")

class Config:
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE = os.environ.get("DATABASE")
    DATABASE_URI = f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE}?ssl=True"
    
    JWT_TOKEN = os.environ.get("JWT_KEY")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_DAYS = 7
    
    
    
    
    