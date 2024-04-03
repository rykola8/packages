# 
# https://docs.python-telegram-bot.org/en/v21.0.1/index.html
# 
# 1. Uzinstalē bibliotēku
# > pip3 install python-telegram-bot
# 
# 2. Uztaisi jaunu Telegram botu un saņem "token" - https://core.telegram.org/bots/features#creating-a-new-bot
#
# 3. Samaini kodā YOUR_TOKEN ar savu token
# 
# 4. Palaid kodu un ieraksti čatā /start
# 
# 5. Apskaties citas komandas - /hello un /echo
#
# 6. Uztaisi jaunu komandu /qrcode, kura pagaidām raksta čata "Building QR code"
#
# 7. Izmantojot kodu no iepriekšēja piemēra (qr-code.py), uzģenerē QR kodu ar jebkādu tekstu un nosūti to čatā ar komandu:
# await update.message.reply_photo('qr.png')
# ! QR kodam jābūt saglabātam "qr.png" failā
# 
# 8. Modificē kodu lai QR koda teksts ģenerētos no tā ko ievadīja lietotājs (apskati /echo komandu)



import qrcode
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("5867819362:AAHITF0lNxnCLiDutgmrMwawZNwN-vl03Ww").build()

# komanda /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm test bot. Type /hello or /echo")

# komanda /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    update.message.reply_photo('')
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {update.effective_user.last_name}')

# komanda /qrcode
async def qr_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img = qrcode.make(update.message.text.replace("/qrcode ", ""))
    img.save("some_file.png")
    await update.message.reply_photo("some_file.png")

# komanda /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I hear: " + update.message.text)

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("qrcode", qr_code))

# sāk bota darbību
app.run_polling()