import asyncio, logging, os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO)

client = TelegramClient(
    StringSession(os.environ["TG_SESSION"]),
    int(os.environ["TG_API_ID"]),
    os.environ["TG_API_HASH"],
)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_action(event):
    try:
        sender = await event.get_sender()
        if getattr(sender, "bot", False):
            return
        async with client.action(event.chat_id, "game"):
            await asyncio.sleep(8)
    except Exception:
        logging.exception("Failed to set game action")

client.start()
client.run_until_disconnected()
