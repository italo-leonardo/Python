import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

application = Application.builder().token("8025292766:AAF77DC0sP2M8Nxgni9mxCMtYOVFtCJ11eg").build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.usarname
    await update.message.reply(f'Ola {user}, esse é o nosso primeiro bot com telegram')

application.add_handler(CommandHandler("start", start))

application.run_polling(allowed_updates=Update.ALL_TYPES)