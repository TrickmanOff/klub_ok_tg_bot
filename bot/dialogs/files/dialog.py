from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from bot.dialogs.common import get_home_button
from bot.dialogs.states import FilesSG


def get_all_files_window() -> Window:
    return Window(
        Const('Все файлы'),
        state=FilesSG.all_files,
    )


def get_hidden_files_window() -> Window:
    return Window(
        Const('Скрытые файлы'),
        state=FilesSG.hidden,
    )


def get_files_window() -> Window:
    return Window(
        Const('Слушаюсь! Вот последние открытые папки.'),
        SwitchTo(Const('Все файлы'), id='all_files', state=FilesSG.all_files),
        SwitchTo(Const('Скрытые'), id='hidden_files', state=FilesSG.hidden),
        get_home_button(),
        state=FilesSG.files,
    )


def get_dialog() -> Dialog:
    return Dialog(
        get_files_window(),
        get_all_files_window(),
        get_hidden_files_window(),
    )
