import asyncio
import pyrogram
import os
from pyrogram import sync
from pathlib import Path
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.on_message import on_bibinto_message
from filters.is_bibinto import check_pm_is_bibinto
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


async def main() -> None:
    load_dotenv()
    BIBINTO_ID = os.getenv("BIBINTO_ID")
    if not BIBINTO_ID:
        return

    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps: list[Client] = []
    for session_file in session_files:
        app = Client(
            str(session_file.stem),
            workdir="data/sessions/",
        )

        async with app as app:
            first_message_scheduled_date = datetime.now(timezone.utc) + timedelta(
                seconds=10
            )
            second_message_scheduled_date = datetime.now(timezone.utc) + timedelta(
                seconds=11
            )
            await app.send_message(
                chat_id=BIBINTO_ID,
                text="/start",
                schedule_date=first_message_scheduled_date,
            )
            await app.send_message(
                chat_id=BIBINTO_ID,
                text="⭐️Кто меня оценил?",
                schedule_date=second_message_scheduled_date,
            )

        app.add_handler(
            MessageHandler(callback=on_bibinto_message, filters=pyrogram.filters.create(func=check_pm_is_bibinto))  # type: ignore
        )
        apps.append(app)

    if apps:
        await sync.compose(apps)


if __name__ == "__main__":
    asyncio.run(main())
