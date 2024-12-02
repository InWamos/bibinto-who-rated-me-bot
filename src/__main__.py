import asyncio
import pyrogram
import os
from pyrogram import sync
from pathlib import Path
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.on_message import on_start_message, on_rate_message
from filters.is_bibinto import check_pm_is_rate_message
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


async def main() -> None:
    load_dotenv()
    BIBINTO_BOT_NICKNAME = os.getenv("BIBINTO_BOT_NICKNAME")
    if not BIBINTO_BOT_NICKNAME:
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
                seconds=20
            )
            await app.send_message(
                chat_id=BIBINTO_BOT_NICKNAME,
                text="/start",
                schedule_date=first_message_scheduled_date,
            )

        app.add_handler(
            MessageHandler(callback=on_start_message, filters=(pyrogram.filters.command("start") & pyrogram.filters.me))  # type: ignore
        )
        app.add_handler(
            MessageHandler(
                callback=on_rate_message,
                filters=pyrogram.filters.create(check_pm_is_rate_message),  # type: ignore
            )
        )
        apps.append(app)

    if apps:
        await sync.compose(apps)


if __name__ == "__main__":
    asyncio.run(main())
