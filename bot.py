import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot tokeninizi buraya ekleyin
TOKEN = 'YOUR_BOT_TOKEN'

# Log ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start komutu
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Merhaba! Ben asistan botunuzum. Size nasıl yardımcı olabilirim?')

# /help komutu
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Yardım menüsü:\n/start - Botu başlat\n/help - Yardım menüsünü göster\n/weather - Hava durumu bilgisi al\n/time - Şu anki zamanı göster')

# /weather komutu
def weather(update: Update, context: CallbackContext) -> None:
    # Burada hava durumu bilgisi eklenebilir
    update.message.reply_text('Hava durumu bilgisini burada göster.')

# /time komutu
def time(update: Update, context: CallbackContext) -> None:
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f'Şu anki zaman: {now}')

# Mesajları yanıtla
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Updater'ı başlat
    updater = Updater(TOKEN)

    # Dispatcher al
    dispatcher = updater.dispatcher

    # Komut işleyicileri ekle
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("weather", weather))
    dispatcher.add_handler(CommandHandler("time", time))

    # Mesaj işleyicisi ekle
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Botu çalıştır
    updater.start_polling()

    # Botu durdurmak için Ctrl+C kullanın
    updater.idle()

if __name__ == '__main__':
    main()
