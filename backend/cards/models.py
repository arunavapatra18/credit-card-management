from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import date

class CreditCard(BaseModel):
    '''
    Pydantic model for Credit Card
    '''
    user_id: UUID4
    card_number: str
    card_issuer: str
    card_variant: str
    card_name: str
    expiry: date
    bill_date: date
    due_date: date
