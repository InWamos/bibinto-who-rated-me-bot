import os

from pyrogram.types import Message


BIBINTO_ID = os.getenv("BIBINTO_ID")

# For example, in a MessageHandler the update argument will be a Message;
# in a CallbackQueryHandler the update will be a CallbackQuery
async def check_pm_is_bibinto(_, __, query: Message) -> bool: # type: ignore
    """Filter to validate that the message from Bibinto bot

    Args:
        _ (_type_): self
        __ (_type_): client
        query (_type_): Message
    """
    if isinstance(query, Message) and BIBINTO_ID: # type: ignore
        return (
            query.from_user.is_self
            and query.from_user.is_bot
            and query.from_user.id == int(BIBINTO_ID)
        )

    return False