import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import links
import markup as nav


load_dotenv()
TOKEN = "7057399024:AAF3gFcl_49UO_2bTWtoAjoaXvoqcHhOD04"
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Welcome to the club, {0.first_name}'
                           .format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message()
async def bot_message(message: types.Message):
    if message.text == 'Generate Gachi':
        await message.reply_photo(links.
                                  gachi[random.
                                        randint(0, len(links.gachi) - 1)])
    else:
        await message.reply('Dude only gachi')


async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())
    print("Hello!")
