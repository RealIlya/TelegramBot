from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

from Stuff.ParseMode import *


class InlineButton:
    client: Client

    def __init__(self, text: str, inlineKeyboardMarkup: InlineKeyboardMarkup):
        self._text = text
        self._keyboardMarkup = inlineKeyboardMarkup

    async def SendKeyboardMarkup(self, message):
        return await InlineButton.client.send_message(message.chat.id, self._text,
                                                      reply_markup=self._keyboardMarkup,
                                                      parse_mode=ParseMode.Markdown)

    async def EditKeyboardMarkup(self, callbackQuery: filters.CallbackQuery):
        return await callbackQuery.edit_message_text(self._text,
                                                     reply_markup=self._keyboardMarkup,
                                                     parse_mode=ParseMode.Markdown)
