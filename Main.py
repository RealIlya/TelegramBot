from Commands import *

app = Client("my_account")
commands = Commands()


@app.on_message(filters.text & filters.private & filters.command("help"))
async def ShowHelpCommand(client: Client, message: filters.Message):
    await commands.ShowHelp(client, message)


@app.on_message(filters.text & filters.private & filters.command("work"))
async def ShowDutiesCommand(client: Client, message: filters.Message):
    await commands.ShowDuties(client, message)


@app.on_message(filters.text & filters.private & filters.command("timetable"))
async def ShowTimetableCommand(client: Client, message: filters.Message):
    await commands.ShowTimetable(client, message)


@app.on_message(filters.text & filters.private & filters.command("time"))
async def ShowTimeCommand(client: Client, message: filters.Message):
    await commands.ShowTime(client, message)


@app.on_message(filters.text & filters.private & filters.command("hw"))
async def ShowHomeworkCommand(client: Client, message: filters.Message):
    await commands.ShowHomework(client, message)


@app.on_message(filters.text & filters.private & filters.command("black"))
async def ShowBlackCommand(client: Client, message: filters.Message):
    await commands.ShowBlack(client, message)


@app.on_message(filters.text & filters.private & filters.command("newhw"))
async def CreateHomeworkCommand(client: Client, message: filters.Message):
    await commands.CreateHomework(client, message)


@app.on_message(filters.text & filters.private & filters.command("echo"))
async def EchoCommand(client: Client, message: filters.Message):
    await commands.Echo(client, message)


def Main():
    app.run()  # Automatically start() and idle()


if __name__ == '__main__':
    Main()
