import asyncio
import pyrogram
from pathlib import Path
from pyrogram.client import Client


async def main() -> None:
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps: list[Client] = []
    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
        apps.append(app)

    if apps:
        pyrogram.sync.compose(apps)


if __name__ == "__main__":
    asyncio.run(main())
