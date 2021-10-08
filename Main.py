from Commands import *

app = Client("my_account")
commands = Commands(app)


@app.on_message(filters.text & filters.command("help"))
async def ShowHelpCommand(_, message: filters.Message):
    return await commands.ShowHelp(message)


@app.on_message(filters.text & filters.command("work"))
async def ShowDutiesCommand(_, message: filters.Message):
    return await commands.ShowDuties(message)


@app.on_message(filters.text & filters.command("timetable"))
async def ShowTimetableCommand(_, message: filters.Message):
    return await commands.ShowTimetable(message)


@app.on_message(filters.text & filters.command("time"))
async def ShowTimeCommand(_, message: filters.Message):
    return await commands.ShowTime(message)


@app.on_message(filters.text & filters.command("hw"))
async def ShowHomeworkCommand(_, message: filters.Message):
    return await commands.ShowHomework(message)


@app.on_message(filters.command("black"))
async def ShowBlackCommand(_, message: filters.Message):
    return await commands.ShowBlack(message)


@app.on_message(filters.text & filters.command("newhw"))
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


def Main():
    app.run()  # Automatically start() and idle()


if __name__ == '__main__':
    Main()
