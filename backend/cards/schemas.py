import uuid
from tortoise import fields, models
from auth.schemas import UserModel

class CreditCardModel(models.Model):
    '''
    Tortoise Model for Credit Card
    '''
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    user_id = fields.UUIDField(foreign_key = "auth.schemas.UserModel.id")
    card_number = fields.CharField(max_length=4, null=False) # Last 4 digits
    card_issuer = fields.CharField(max_length=255, null = False)    
    card_variant = fields.CharField(max_length=32, null=False)      
    card_name = fields.CharField(max_length=128, null=False)
    expiry = fields.DateField()
    bill_date = fields.DateField()
    due_date = fields.DateField()
    
    # For reverse lookup
    user = fields.ForeignKeyField('auth.schemas.UserModel', related_name='credit_cards')