from fastapi import APIRouter, Depends
from backend.auth.models import User
from backend.cards.models import CreditCard

router = APIRouter()

@router.post("/card", response_model=CreditCard)
async def create_credit_card(card: CreditCard, user: User = Depends(get_current_user))