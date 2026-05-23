import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# تفعيل تسجيل الأخطاء لرؤية ما يحدث
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("تم استلام أمر /start") # سيظهر هذا في الـ Logs في Railway
    await update.message.reply_text("✅ البوت يعمل بنجاح ويستقبل الأوامر!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"تم استلام رسالة: {update.message.text}")
    await update.message.reply_text(f"وصلني منك: {update.message.text}")

if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        print("خطأ: التوكن غير موجود!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
        print("البوت بدأ الآن...")
        app.run_polling()
