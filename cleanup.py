from telethon import TelegramClient
from datetime import datetime, timedelta
import asyncio



from telethon import TelegramClient
from datetime import datetime, timedelta, timezone  # ← added timezone
import asyncio

API_ID   = 24174270
API_HASH = 'bef8127ecfa59bb7866b182872ca57eb'
DAYS_UNUSED = 90
# make this UTC-aware so it compares cleanly with Telegram’s dates
UNUSED_BEFORE = datetime.now(timezone.utc) - timedelta(days=DAYS_UNUSED)

async def main():
    client = TelegramClient('cleanup_session', API_ID, API_HASH)
    await client.start()
    # ...
    async for dialog in client.iter_dialogs():
        last_date = dialog.message.date if dialog.message else None
        # now this comparison will work:
        if last_date and last_date < UNUSED_BEFORE:
            # mark as unused…
            pass
    # …
