import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📲 Написать в WhatsApp", url="https://wa.me/79616784444")],
        [InlineKeyboardButton("🔗 Подробнее на Avito", url="https://www.avito.ru/sochi/doma_dachi_kottedzhi/4-k._dom_109_m_4865915984")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🏡 Добро пожаловать!\n\n"
        "📍Домик с видом на море.\n"
        "🛏️ 4 комнаты, 109 м²\n"
        "🌿 Закрытая территория, все коммуникации"
    )
    await update.message.reply_text(text, reply_markup=reply_markup)

if __name__ == '__main__':
    keep_alive()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Устанавливаем webhook
    import requests
    set_webhook_url = os.getenv("WEBHOOK_URL")
    webhook_url = f"{set_webhook_url}/webhook"
    requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}")

    app.run_polling()

    
   
