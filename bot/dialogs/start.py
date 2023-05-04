from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Start
from aiogram_dialog.widgets.text import Const

from bot.dialogs.states import StartSG, BrowserSG, FilesSG


def get_start_window() -> Window:
    return Window(
        Const("Последнее, что Вы просматривали. К чему хотите вернуться?"),
        # Button(Const("Браузер"), id="browser", on_click)
        Start(Const("Браузер"), id="browser", state=BrowserSG.browser),
        Start(Const("Файлы"), id="files", state=FilesSG.files),
        state=StartSG.start,
    )

def get_dialog() -> Dialog:
    dialog = Dialog(
       get_start_window(),
    )
    return dialog
