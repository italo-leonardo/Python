from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import json, random

FLASHCARD_GAME, FLASHCARD_REPLY = range(2)

mensagens_acerto = [
    "🎉 Parabéns! Você acertou em cheio! 🚀",
    "🔥 Uau! Você mandou muito bem! 🎯",
    "👏 Isso aí! Você está no caminho certo! 🌟",
    "🎯 Acertou na mosca! Excelente trabalho! 🏆",
    "💡 Brilhante! Você está arrebentando! 🤩",
    "🚀 Boom! Você detonou nessa! 🎇",
    "🏅 Medalha de ouro para você! Muito bom! 🥇",
    "🎊 Sim! Você está cada vez melhor! 💪",
    "🧠 Mente afiada! Você acertou de novo! 🔥",
    "🌟 Genial! Continue assim! O sucesso te espera! 🚀"
]

mensagens_erro = [
    "😬 Opa! Quase lá! Tente mais uma vez! 🔄",
    "❌ Errado, mas não desista! Você está aprendendo! 📚",
    "🤔 Hmmm... Não foi dessa vez! Bora tentar de novo? 🔄",
    "😅 Perto! Continue tentando, você consegue! 💪",
    "🚧 Erros fazem parte do caminho! Vamos lá! 🏗️",
    "🔄 Não foi dessa vez, mas cada erro te deixa mais forte! 💡",
    "💭 Opa, pense mais um pouco! Você chega lá! 🎯",
    "⚠️ Errar faz parte do aprendizado! Tente de novo! 📈",
    "🤖 Erros? Só mais um passo para o acerto! Bora! 🚀",
    "🔥 Você está quase lá! Um pouco mais de esforço e acerta! 🏆"
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username
    await update.message.reply_text(f"Olá {user}, esse é o nosso primeiro bot com telegram")


async def flashcard_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # global item
    item = random.choice(dados)
    
    context.user_data['item'] = item
    
    await update.message.reply_photo(
        photo=open(item['imagem'],'rb'),
        caption='O que é isso? Descreva o objeto em inglês.'
    )
    return FLASHCARD_REPLY


async def sair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bye!")
    return ConversationHandler.END


async def flashcard_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = update.message.text
    # global item 
    item = context.user_data.get('item', '')
    
    if reply.lower() == item['nome_em_us'].lower():
        await update.message.reply_text(random.choice(mensagens_acerto))
    else:
        await update.message.reply_text(random.choice(mensagens_erro))
    
    reply_keyboard = [["/continuar", "/sair"]]
    
    await update.message.reply_text("Deseja continuar?\n",
                                    reply_markup=ReplyKeyboardMarkup(
                                        reply_keyboard, one_time_keyboard=True,
                                        input_field_placeholder='Continuar?'
                                    ))
    
    return FLASHCARD_GAME

with open('database.json', 'r') as arquivo:
    dados = json.load(arquivo)

application = Application.builder().token('').build()
    
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