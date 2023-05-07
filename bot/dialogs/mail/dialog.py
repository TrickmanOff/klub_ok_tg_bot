import os
from typing import List

from aiogram.enums import ParseMode
from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from bot.dialogs.common import get_home_button
from bot.dialogs.mail.emails import emails
from bot.dialogs.states import MailSG


def get_back_to_mail_button() -> SwitchTo:
    return SwitchTo(Const('Ко всем письмам'), id='back_to_mail', state=MailSG.mail)


def get_filepath(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'files', filename)


def get_letter_window(id: str) -> Window:
    widgets = [Const(emails[id].content)]
    if emails[id].filename is not None:
        widgets.append(StaticMedia(
            path = get_filepath(emails[id].filename),
            type=ContentType.PHOTO,
        ))
    return Window(
        *widgets,
        get_back_to_mail_button(),
        get_home_button(),
        state=getattr(MailSG, id),
        parse_mode=ParseMode.MARKDOWN,
    )


def get_mail_windows() -> List[Window]:
    mail_window = Window(
        Const('Конечно! Ой, у Вас столько непрочитанных писем. Последние 3 письма от Водяного, Василисы и неизвестных отправителей. Какое открыть?'),
        *[SwitchTo(Const(email.sender), id=f'email_from_{id}', state=getattr(MailSG, id)) for id, email in emails.items()],
        get_home_button(),
        state=MailSG.mail,
    )
    return [mail_window] + [get_letter_window(id) for id in emails]


def get_dialog() -> Dialog:
    return Dialog(
        *get_mail_windows(),
    )
