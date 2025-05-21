import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import time
import threading

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "7560560212:AAE4e4J1J867tlasOBx7Ovv3faKtK5sDS_nU"  # Твой токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-помощник по поиску удалённой работы.")

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здесь будет список актуальных вакансий (пока заглушка).")

def run_schedule(app):
    async def job_task():
        chat_id = "377810740"  # Твой chat_id
        await app.bot.send_message(chat_id=chat_id, text="Доброе утро! Вот новые вакансии на сегодня (заглушка).")

    schedule.every().day.at("09:00").do(lambda: app.create_task(job_task()))

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jobs", jobs))

    async def main():
        await app.initialize()
        # Запускаем планировщик в отдельном потоке
        scheduler_thread = threading.Thread(target=run_schedule, args=(app,), daemon=True)
        scheduler_thread.start()

        await app.start()
        await app.updater.start_polling()
        await app.updater.idle()

    import asyncio
    asyncio.run(main())
