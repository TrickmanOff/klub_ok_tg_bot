import asyncio
import os
from typing import List

from aiogram.types import CallbackQuery, ContentType
from aiogram_dialog import BaseDialogManager, Dialog, DialogManager, Window 
from aiogram_dialog.widgets.kbd import Button, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const
from aiogram.enums import ParseMode

from bot.dialogs.common import get_home_button
from bot.dialogs.states import FilesSG


def get_back_to_files_button() -> SwitchTo:
    return SwitchTo(Const('Назад в файлы'), id='back_to_files', state=FilesSG.files)


def get_filepath(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'files', filename)


def get_cat_window() -> Window:
    return Window(
        Const('Это же Ваш сын! Очень мило 😚'),
        StaticMedia(
            path = get_filepath('cat.jpeg'),
            type=ContentType.PHOTO,
        ),
        get_back_to_files_button(),
        get_home_button(),
        state=FilesSG.cat_file,
    )


def get_scheme_window() -> Window:
    return Window(
        Const('Ничего себе, Кот! Вы и правда гениальный учёный. Даже мой искусственный интеллект ничего не понимает в этих схемах.'),
        StaticMedia(
            path = get_filepath('scheme.jpeg'),
            type=ContentType.PHOTO,
        ),
        get_back_to_files_button(),
        get_home_button(),
        state=FilesSG.scheme_file,
    )


def get_all_files_windows() -> List[Window]:
    all_files_window = Window(
        Const('Все файлы'),
        SwitchTo(Const('chertezh_finalniy.png'), id='scheme_file', state=FilesSG.scheme_file),
        SwitchTo(Const('IMG_4305.jpeg'), id='cat_file', state=FilesSG.cat_file),
        state=FilesSG.all_files,
    )
    return [all_files_window, get_scheme_window(), get_cat_window()]


def get_bug_return_window() -> Window:
    msg = 'Простите, кажется, это какой-то баг. Возвращаю вас в файлы!'
    return Window(
        Const(msg),
        state=FilesSG.bug_return,
    )


async def hidden_background(callback: CallbackQuery, manager: BaseDialogManager):
    await asyncio.sleep(10)
    await manager.switch_to(FilesSG.bug_return)
    await asyncio.sleep(5)
    await manager.done()


async def to_hidden_file(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(FilesSG.files)
    await manager.start(state=FilesSG.hidden_file)
    asyncio.create_task(hidden_background(c, manager.bg()))


def get_hidden_file_windows() -> List[Window]:
    msg = """\
Узнай, что же случилось с Котом и какие у этого будут последствия, в демоверсии игры *Лукоморье 2084: На закате корпораций!*

Следи за обновлениями:
https://t.me/lkmr2084
https://vk.com/lkmr2084
"""
    return [Window(
        Const(msg),
        # SwitchTo(Const('Простите, кажется, это какой-то баг. Возвращаю вас в файлы!'), id='hidden_back_to_files', state=FilesSG.files),
        state=FilesSG.hidden_file,
        parse_mode=ParseMode.MARKDOWN,
    ), get_bug_return_window()]


def get_hidden_files_windows() -> List[Window]:
    hidden_window = Window(
        Const('У Вас только один скрытый файл под названием LK84. Открываю?'),
        SwitchTo(Const('Нет'), id='back_to_files', state=FilesSG.files),
        # SwitchTo(Const('Да'), id='open_hidden_file', state=FilesSG.hidden_file),
        Button(Const('Да'), id='open_hidden_file', on_click=to_hidden_file),
        state=FilesSG.hidden,
    )
    return [hidden_window, *get_hidden_file_windows()]


def get_files_windows() -> List[Window]:
    files_window = Window(
        Const('Слушаюсь! Вот последние открытые папки.'),
        SwitchTo(Const('Все файлы'), id='all_files', state=FilesSG.all_files),
        SwitchTo(Const('Скрытые'), id='hidden_files', state=FilesSG.hidden),
        get_home_button(),
        state=FilesSG.files,
    )
    return [files_window, *get_all_files_windows(), *get_hidden_files_windows()]


def get_dialog() -> Dialog:
    return Dialog(
        *get_files_windows(),
    )
