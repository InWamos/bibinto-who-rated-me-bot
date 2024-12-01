import asyncio
import os
from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.client import Client
from random import randint

MAX_CAP: str | None = os.getenv("MAX_CAP")


async def on_rate_message(client: Client, message: Message) -> None:
    reply_markup = message.reply_markup

    if isinstance(reply_markup, InlineKeyboardMarkup):
        message_keyboard = reply_markup.inline_keyboard[0][0]

        if "⭐️Оценить" == message_keyboard.text:
            try: 
                print("yes")
                await asyncio.sleep(1)
                await message.click(0)
                await asyncio.sleep(2)
                new_message = await client.get_messages(
                    chat_id=message.chat.id, message_ids=message.id
                )
                await asyncio.sleep(1)
                if isinstance(new_message, Message):
                    random_rating: int = randint(7, 10)
                    await new_message.click(random_rating)
            except TimeoutError:
                pass


async def on_start_message(client: Client, message: Message) -> None:
    if MAX_CAP:
        for _ in range(int(MAX_CAP)):
            await client.send_message(chat_id=message.chat.id, text="⭐️Кто меня оценил?")
            await asyncio.sleep(5)