import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# دالة القائمة الرئيسية (تشبه القائمة التي أرسلتها في الصورة)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 نظام الفحص الذكي", callback_data='check')],
        [InlineKeyboardButton("🌐 بيانات استخباراتية", callback_data='data')],
        [InlineKeyboardButton("🛡 قائمة المحظورين", callback_data='blacklist')],
        [InlineKeyboardButton("🛠 لوحة التحكم السيبرانية", callback_data='control')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🛡 **منظمة الاستخبارات السيبرانية**\n\nأهلاً بك أيها العميل. اختر المهمة المطلوبة:", reply_markup=reply_markup)

# معالجة ضغطات الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check':
        await query.edit_message_text("🔍 **نظام الفحص:** أرسل رقم الهاتف أو اليوزر للبدء...")
    elif query.data == 'data':
        await query.edit_message_text("🌐 **البيانات المتاحة:** جاري الوصول إلى قواعد البيانات المفتوحة...")
    elif query.data == 'blacklist':
        await query.edit_message_text("🛡 **قائمة المحظورين:** لا توجد بلاغات نشطة حالياً.")
    elif query.data == 'control':
        await query.edit_message_text("🛠 **التحكم:** البوت متصل بالخادم بنسبة 100%.")

if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    
    print("المنظومة تعمل الآن بكامل قوتها...")
    app.run_polling()
    
