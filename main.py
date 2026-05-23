import os
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("البوت يعمل الآن يا بطل!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ.get("TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
