from pydantic import UUID4

from backend.cards.models import CreditCard
from backend.cards.schemas import CreditCardModel


class CardsDatabaseUtils:
    async def add_card(card: CreditCardModel):
        await card.save()

    async def check_for_existing_card(user_id: UUID4, card: CreditCard):
        existing = await CreditCardModel.filter(
            card_number = card.card_number,
            card_name = card.card_name,
            card_variant = card.card_variant,
            user_id = user_id
        ).first()
        
        if existing:
            return True
        return False
