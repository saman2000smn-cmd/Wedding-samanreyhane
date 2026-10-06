from datetime import date
from telegram import Bot
import asyncio

# 👇 توکن رباتت را بین این دو علامت قرار بده
BOT_TOKEN = os.environ["BOT_TOKEN"]

# 👇 آیدی کانال
CHANNEL_ID = "@samanreyhane"

# 👇 تاریخ روز پیوند
WEDDING_DATE = date(2026, 12, 20)


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


if name == "main":
    asyncio.run(send_countdown())
