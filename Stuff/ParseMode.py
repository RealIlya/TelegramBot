class ParseMode:
    Markdown = "markdown"
    Combined = "combined"


def GetOnlyText(text: str):
    return text.split(' ')[1:]
