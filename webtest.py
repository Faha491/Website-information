import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "6092586617:AAGG--8_tLAUJhVUAWVI3rCx8VvK97JZoxI"  # Replace with your bot's token

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Hello! Send me a domain name, and I'll fetch WHOIS info.")

def whois_lookup(update: Update, context: CallbackContext):
    website = update.message.text.strip()

    if not website:
        update.message.reply_text("⚠️ Please enter a valid domain name.")
        return

    try:
        result = subprocess.run(["whois", website], capture_output=True, text=True, check=True)
        update.message.reply_text(f"🔍 WHOIS Info for {website}:\n\n{result.stdout[:4000]}")
    except FileNotFoundError:
        update.message.reply_text("❌ WHOIS command not found! Please install WHOIS.")
    except subprocess.CalledProcessError:
        update.message.reply_text("⚠️ Failed to fetch WHOIS information.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, whois_lookup))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
