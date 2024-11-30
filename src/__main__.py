import asyncio
import pyrogram
from pyrogram import sync
from pathlib import Path
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.on_message import on_bibinto_message
from filters.is_bibinto import check_pm_is_bibinto
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps: list[Client] = []
    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
        app.add_handler(
            MessageHandler(callback=on_bibinto_message, filters=pyrogram.filters.create(func=check_pm_is_bibinto))  # type: ignore
        )
        apps.append(app)

    if apps:
        await sync.compose(apps)


if __name__ == "__main__":
    asyncio.run(main())
