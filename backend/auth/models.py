from pydantic import BaseModel, UUID4

class User(BaseModel):
    '''
    Pydantic model for User
    '''
    name: str
    email: str
    password: str
    
class LoginUser(BaseModel):
    '''
    Pydantic model for login user
    '''
    email: str
    password: str
