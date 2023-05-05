from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const


def get_home_button() -> Cancel:
    return Cancel(Const('На главную'), id='home')
