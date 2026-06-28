from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import google.generativeai as genai
from config import TELEGRAM_TOKEN, GEMINI_API_KEY, GEMINI_MODEL

# Configurar Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 ¡Hola! Soy tu bot con Gemini.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text

    try:
        respuesta = model.generate_content(mensaje)
        await update.message.reply_text(respuesta.text)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
