from Stuff.ParseMode import *


class Errors:

    @staticmethod
    def PrintError(message, textError):
        return message.reply_text("**--{0}--**".format(textError),
                                  parse_mode=ParseMode.Markdown, quote=True)
