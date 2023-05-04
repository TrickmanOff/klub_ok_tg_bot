from typing import List

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from bot.dialogs.browser.article_importer import articles
from bot.dialogs.common import get_home_button
from bot.dialogs.states import BrowserSG


def get_articles_windows() -> List[Window]:
    return [
        Window(
            Const(article.content),
            SwitchTo(Const("К другим статьям"), id="return", state=BrowserSG.browser),
            state=getattr(BrowserSG, id),
            parse_mode=ParseMode.MARKDOWN,
        )
        for id, article in articles.items()
    ]


def get_browser_window() -> Window:
    switches_to_articles = [
        SwitchTo(Const(article.title), id=id, state=getattr(BrowserSG, id))
        for id, article in articles.items()
    ]
    return Window(
        Const("Открываю! Похоже Вы недавно начинали читать эти статьи."),
        get_home_button(),
        *switches_to_articles,
        state=BrowserSG.browser,
    )


def get_dialog() -> Dialog:
    return Dialog(
       get_browser_window(),
       *get_articles_windows(),
    )
