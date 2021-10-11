from Commands import *

app = Client("my_account")
commands = Commands(app)
timetableButtons = [f"t{i}" for i in range(0, 7)]


@app.on_message(filters.text & filters.command("help"))
async def ShowHelpCommand(_, message: filters.Message):
    return await commands.ShowHelp(message)


@app.on_message(filters.text & filters.command("work"))
async def ShowDutiesCommand(_, message: filters.Message):
    return await commands.ShowDuties(message)


@app.on_message(filters.text & filters.command("timetable"))
async def ChooseTimetableCommand(_, message: filters.Message):
    return await commands.ChooseTimetable(message)


@app.on_message(filters.text & filters.command("time"))
async def ShowTimeCommand(_, message: filters.Message):
    return await commands.ShowTime(message)


@app.on_message(filters.text & filters.command("hw"))
async def ShowHomeworkCommand(_, message: filters.Message):
    return await commands.ShowHomework(message)


@app.on_message(filters.command("gmeme"))
async def ShowGeneratedMemeCommand(_, message: filters.Message):
    return await commands.ShowBlack(message)


@app.on_message(filters.command("black"))
async def ShowBlackCommand(_, message: filters.Message):
    return await commands.ShowBlack(message)


@app.on_message(filters.command("newhw"))
async def CreateHomeworkCommand(_, message: filters.Message):
    return await commands.CreateHomework(message)


@app.on_message(filters.text & filters.command("echo"))
async def EchoCommand(_, message: filters.Message):
    return await commands.Echo(message)


@app.on_message(filters.text & filters.command("repeat"))
async def RepeatCommand(_, message: filters.Message):
    return await commands.Repeat(message)


@app.on_message(filters.text & filters.command("ghoul"))
async def GhoulCommand(_, message: filters.Message):
    return await commands.Ghoul(message)


@app.on_callback_query()
async def ShowTimeTableCallback(_, callbackQuery: filters.CallbackQuery):
    if callbackQuery.data in timetableButtons:
        return await commands.ShowTimetable(callbackQuery)
    if callbackQuery.data == "t-1":
        return await commands.AgainChooseTimetable(callbackQuery)


def Main():
    app.run()  # Automatically start() and idle()


if __name__ == '__main__':
    Main()
