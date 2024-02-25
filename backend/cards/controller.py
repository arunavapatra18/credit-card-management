from pydantic import UUID4
from backend.exceptions import CustomException
from backend.cards.models import CreditCard
from backend.cards.database import CardsDatabaseUtils
from backend.cards.schemas import CreditCardModel


async def add_new_card(user_id: UUID4, card: CreditCard):
    try:
        card_exists = await CardsDatabaseUtils.check_for_existing_card(user_id, card)

        if card_exists:
            raise CustomException.CardAlreadyAddedException
        
        card_model = await CreditCardModel.create(**card.model_dump())

        await CardsDatabaseUtils.add_card(card=card_model)
    
    except CustomException.DatabaseOperationException as e:
        raise CustomException.DatabaseOperationException(f"Saving card to database failed! Error message = {e}")