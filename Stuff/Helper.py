import time


class Helper:
    @staticmethod
    async def SetDelay(seconds, func, text):
        time.sleep(seconds)
        await func(text)
