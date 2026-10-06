from datetime import date
from telegram import Bot
import asyncio
import os


# تاریخ روز پیوند
WEDDING_DATE = date(2026, 12, 20)

# آیدی کانال
CHANNEL_ID = "@samanreyhane"

# توکن از GitHub Secret خوانده می‌شود
BOT_TOKEN = os.environ["BOT_TOKEN"]


def get_days_left():
    today = date.today()
    return (WEDDING_DATE - today).days


def create_message(days_left):

    if days_left > 0:
        return f"💍 {days_left} روز تا پیوند 📆❤️"

    if days_left == 0:
        return """💍❤️ امروز روز پیوندمونه! ❤️💍

🎉 روزمون مبارک عشقم 🥹❤️

از امروز، قشنگ‌ترین فصل زندگی‌مون شروع میشه... 💞✨"""

    return None


async def send_countdown():

    bot = Bot(token=BOT_TOKEN)

    days_left = get_days_left()
    message = create_message(days_left)

    if message:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message
        )

    await bot.close()


if __name__ == "__main__":
    asyncio.run(send_countdown())
