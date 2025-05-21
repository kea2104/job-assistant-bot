import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import asyncio

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = 'сюда вставь свой токен'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я помогу тебе с удалённой работой.")

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вот вакансии на сегодня (заглушка).")

async def send_daily_message(app):
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)

def job_task():
    app.bot.send_message(chat_id='сюда chat_id', text="Доброе утро! Вот новые вакансии на сегодня (заглушка).")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))

schedule.every().day.at("09:00").do(job_task)

app.run_polling()
