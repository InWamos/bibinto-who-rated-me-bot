import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.client import Client


async def on_bibinto_message(client: Client, message: Message) -> None:
    reply_markup = message.reply_markup

    if isinstance(reply_markup, InlineKeyboardMarkup):
        message_keyboard = reply_markup.inline_keyboard[0][0]
        print(message_keyboard.text, type(message_keyboard))
        if "Оценить" in message_keyboard.text:
            await asyncio.sleep(1)
            await message.click(0)
            await asyncio.sleep(1)
            new_message = await client.get_messages(
                chat_id=message.chat.id, message_ids=message.id
            )
            await asyncio.sleep(1)
            if isinstance(new_message, Message):
                await new_message.click(3, 1)
