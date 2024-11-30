import os

from pyrogram.types import Message
from pyrogram.client import Client

BIBINTO_ID = os.getenv("BIBINTO_ID")

# For example, in a MessageHandler the update argument will be a Message;
# in a CallbackQueryHandler the update will be a CallbackQuery
async def check_pm_is_bibinto(_: object, __: Client, query: Message) -> bool:
    """Filter to validate that the message from Bibinto bot

    Args:
        _ (_type_): self
        __ (_type_): client
        query (_type_): Message
    """
    if BIBINTO_ID:
        return (
            not query.from_user.is_self
            and query.from_user.is_bot
            and query.from_user.id == int(BIBINTO_ID)
        )

    return False