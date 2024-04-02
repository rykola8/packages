# 1. Uztaisiet komandu /weather-riga kurā atspoguļos tekošo temperatūru (airTemperature)
#    Izmantojiet datus no https://api.meteo.lt/v1/places/riga/forecasts/long-term un piemēru no https://github.com/19th/debugging2/blob/main/1_city_info.py


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("YOUR_TOKEN").build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm test bot")

app.add_handler(CommandHandler("start", start))

# sāk bota darbību
app.run_polling()