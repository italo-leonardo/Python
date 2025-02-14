from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

FLASHCARD_GAME, FLASHCARD_REPLY = range(2)

application = Application.builder().token('8025292766:AAF77DC0sP2M8Nxgni9mxCMtYOVFtCJ11eg').build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username
    await update.message.reply_text(f"Olá {user}, esse é o nosso primeiro bot com telegram")


async def flashcard_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open('/img/images.jpg','rb'),
        caption='O que é isso? Descreva o objeto em inglês.'
    )
    return FLASHCARD_REPLY


async def sair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bye!")
    return ConversationHandler.END


async def flashcard_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = update.message.text
    
    if reply == 'apple':
        await update.message.reply_text("acertou")
    else:
        await update.message.reply_text("errou")
    
    reply_keyboard = [["/continuar", "/sair"]]
    
    await update.message.reply_text("Deseja continuar?\n",
                                    reply_markup=ReplyKeyboardMarkup(
                                        reply_keyboard, one_time_keyboard=True,
                                        input_field_placeholder='Continuar?'
                                    ))
    
    return FLASHCARD_GAME

    
application.add_handler(CommandHandler("start", start))
application.add_handler(ConversationHandler(
    entry_points=[
        CommandHandler("flashcard", flashcard_game),
    ],
    states={
        FLASHCARD_REPLY: [
            MessageHandler(filters.TEXT, flashcard_reply)
        ],
        FLASHCARD_GAME: [
            CommandHandler('continuar', flashcard_game)
        ]
    },
    fallbacks=[
        CommandHandler("sair", sair)
    ]
))

application.run_polling(allowed_updates=Update.ALL_TYPES)