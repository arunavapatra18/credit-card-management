from pydantic import BaseModel, UUID4, Field
from typing import Optional
from datetime import date

class CreditCard(BaseModel):
    '''
    Pydantic model for Credit Card
    '''
    user_id: Optional[UUID4] = None
    card_number: str
    card_issuer: str
    card_variant: str
    card_name: str
    bill_date: date
    due_date: date
