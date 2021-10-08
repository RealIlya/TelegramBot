import json
import random


class Duties:

    def __init__(self):
        with open("Students.json", "r", encoding="utf-8") as file:
            self._dutiesList = json.load(file)

    def GetRandomDuties(self):
        first = self._dutiesList[random.randint(0, len(self._dutiesList) - 1)]
        second = self._dutiesList[random.randint(0, len(self._dutiesList) - 1)]

        return [first['Name'] + " " + first['Surname'], second['Name'] + " " + second['Surname']]
