import sys
# temporary measure to find 'bot' package
sys.path.append('/Users/trickman/sonya_tg_bot')

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogManager, StartMode, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const
from aiogram.filters.command import Command

import asyncio
import os


from bot.dialogs.start import StartSG
from bot.dialogs.start import get_dialog as get_start_dialog
from bot.dialogs.browser.dialog import get_dialog as get_browser_dialog
from bot.dialogs.files.dialog import get_dialog as get_files_dialog


# storage = MemoryStorage()
storage = RedisStorage.from_url('redis://localhost:6379/0', key_builder=DefaultKeyBuilder(with_destiny=True))
dp = Dispatcher(storage=storage)

def register_dialogs() -> None:
    dialog_creators = [
        get_start_dialog,
        get_browser_dialog,
        get_files_dialog,
    ]
    for dialog_creator in dialog_creators:
        dp.include_router(dialog_creator())
    setup_dialogs(dp)


bot = Bot(token=os.environ['TELEGRAM_TOKEN'])


@dp.message(Command("start"))
async def start(m: Message, dialog_manager: DialogManager):
    # Important: always set `mode=StartMode.RESET_STACK` you don't want to stack dialogs
    # идентификатор 
    await dialog_manager.start(StartSG.start, mode=StartMode.RESET_STACK)


async def main():
    register_dialogs()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
