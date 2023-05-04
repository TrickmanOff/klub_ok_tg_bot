# a separate file to avoid circular import dependencies
from aiogram.fsm.state import State, StatesGroup

from bot.dialogs.browser.article_importer import articles


class StartSG(StatesGroup):
    start = State()


class BrowserSG(StatesGroup):
    browser = State()

    for article_id in articles:
        locals()[article_id] = State()


class FilesSG(StatesGroup):
    files = State()
    
    all_files = State()
    hidden = State()
