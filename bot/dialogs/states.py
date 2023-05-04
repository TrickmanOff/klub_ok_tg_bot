# a separate file to avoid circular import dependencies
from aiogram.fsm.state import State, StatesGroup

from bot.dialogs.browser.article_importer import articles
from bot.dialogs.mail.emails import emails


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
    scheme_file = State()
    cat_file = State()
    hidden_file = State()


class MailSG(StatesGroup):
    mail = State()

    for email_id in emails:
        locals()[email_id] = State()
