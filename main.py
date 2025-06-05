import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📞 Контакт: +79616784444", callback_data="contact_info")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = (
        "🏡 Добро пожаловать!\n\n"
        "📍Предлагаем уютный дом в Адлере, всего в 10 минутах от пляжа.\n"
        "🛏️ 4 комнаты, 109 м²\n"
        "🌿 Закрытая территория, центральные коммуникации"
    )
    await update.message.reply_text(text, reply_markup=reply_markup)

if __name__ == '__main__':
    keep_alive()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
