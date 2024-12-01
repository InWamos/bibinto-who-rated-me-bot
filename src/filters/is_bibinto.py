import os

from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.client import Client

BIBINTO_ID = os.getenv("BIBINTO_ID")


# For example, in a MessageHandler the update argument will be a Message;
# in a CallbackQueryHandler the update will be a CallbackQuery
async def check_pm_is_rate_message(_: object, __: Client, query: Message) -> bool:
    """Filter to validate that the message from Bibinto bot

    Args:
        _ (_type_): self
        __ (_type_): client
        query (_type_): Message
    """
    if BIBINTO_ID:
        if isinstance(query.reply_markup, InlineKeyboardMarkup):
            return True

    return False
