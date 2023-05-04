from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot.dialogs.states import StartSG


def get_home_button() -> Start:
    return Start(Const('На главную'), id='home', state=StartSG.start)
