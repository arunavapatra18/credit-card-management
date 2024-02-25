from fastapi import APIRouter, Depends
from pydantic import UUID4
from backend.cards.controller import add_new_card
from backend.cards.models import CreditCard
from backend.auth.database import get_current_user
from backend.cards.schemas import CreditCardModel

cards_router = APIRouter()

@cards_router.post("/cards/add")
async def add_credit_card(card: CreditCard, user_id: UUID4 = Depends(get_current_user)):
    card.user_id = user_id
    new_card = await add_new_card(user_id = user_id, card=card)
    return {"message": "Card added successfully"}