import uuid
from tortoise import fields
from tortoise.models import Model
import bcrypt

class UserModel(Model):
    '''
    Tortoise ORM Model for User
    '''
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=False, unique=True)
    password = fields.CharField(max_length=255, null=False)
    
    class Meta:
        table = "users"
        
    def generate_password_hash(self, password_str: str, salt: str):
        '''
        Method to hash passwords
        '''
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_str.encode('utf8'), salt)
        self.password = hashed_password.decode("utf8")
        
    def verify_password(self, password_str: str):
        '''
        Method to verify input password with hashed password from the db
        '''
        return bcrypt.checkpw(
            password_str.encode("utf8"),
            self.password.encode("utf8")
        )
    