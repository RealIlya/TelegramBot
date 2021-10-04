import datetime as dt
import random as r
import time
from pyrogram import Client, filters
from pyrogram.types import *


class Commands:

    def __init__(self):
        self._duties = [str(i) for i in range(1, 26)]

    @property
    def GetRandom(self):
        first = self._duties[r.randint(1, len(self._duties))]
        second = self._duties[r.randint(1, len(self._duties))]

        return ', '.join([first, second])

    async def ShowHelp(self, client: Client, message: filters.Message):
        return await client.send_message(message.chat.id, "Для просмотра дежурных /work.\n"
                                                          "Расписание - /timetable.\n"
                                                          "Когда я? - /time \n"
                                                          "Домашнее задание - /hw.\n"
                                                          "Демотиватор - /black [картинка].\n\n"
                                                          "Сохранить домашнее задание в бота -\n"
                                                          "/newhw [день недели] [предмет] [картинка]",
                                         reply_markup=ReplyKeyboardMarkup([
                                             [KeyboardButton("/work"), KeyboardButton("/timetable"),
                                              KeyboardButton("/time")],
                                             [KeyboardButton("/hw"), KeyboardButton("/black"), KeyboardButton("/newhw")]
                                         ], resize_keyboard=True, one_time_keyboard=True))

    async def ShowDuties(self, client: Client, message: filters.Message):
        return await client.send_message(message.chat.id, f"Дежурные сегодня - {self.GetRandom}")

    async def ShowTimetable(self, client: Client, message: filters.Message):
        pass

    async def ShowTime(self, client: Client, message: filters.Message):
        return await client.send_message(message.chat.id, "Дата: {:%m-%d-%y} \n".format(dt.datetime.today()) +
                                         "Время: {:%H:%M:%S}".format(dt.datetime.today()))

    async def ShowHomework(self, client: Client, message: filters.Message):
        pass

    async def ShowBlack(self, client: Client, message: filters.Message):
        pass

    async def CreateHomework(self, client: Client, message: filters.Message):
        pass

    async def Echo(self, client: Client, message: filters.Message):
        textList = message.text.split(' ')
        if len(textList) < 4:
            return await client.send_message(message.chat.id, "Некорректрный ввод")

        duration = round(float(textList.pop(1))) if textList[1] is not None else 0
        delay = float(textList.pop(1)) if textList[1] is not None else 0

        for i in range(duration):
            time.sleep(delay)
            await client.send_message(message.chat.id, ' '.join(textList[1:]))
