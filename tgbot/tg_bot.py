import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from random import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Рад приветствовать тебя! Меня зовут бот yarbot.\nВот что я умею делать:")
    await help(update, context)
    context.user_data['mode'] = 'undefined'


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="/start\n/help\n/guess_the_number\n/recommend_film\n/recommend_food")


async def guess_the_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    attempts = 5
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Угадай-ка!\nУгадай число от 1 до 100\nу Вас {attempts} попыток!")
    context.user_data['number'] = randint(1, 100)
    context.user_data['mode'] = 'guess'
    context.user_data['attempts_left'] = attempts


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get('mode', 'undefined')
    if mode == 'guess':
        if update.message.text.isdigit():
            num = int(update.message.text)
            if num == context.user_data.get('number'):
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Вы угадали!')
                context.user_data['mode'] = 'undefined'
                return

            context.user_data['attempts_left'] = context.user_data.get('attempts_left') - 1
            if context.user_data.get('attempts_left') == 0:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f'Вы не угадали это была последняя попытка! Я загадывал число {context.user_data.get('number')} ')
                context.user_data['mode'] = 'undefined'
                return
            if num > context.user_data.get('number'):
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f'Я загадал число меньше! У вас осталось {context.user_data.get('attempts_left')} попыток')
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f'Я загадал число больше! У вас осталось {context.user_data.get('attempts_left')} попыток')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Введите число!')
    elif mode == 'film':
        if update.message.text == 'ужастик':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='Хороший выбор, можно посмотреть "Чужой", "Пятница 13-тое" или "Техаская резня бензопилой"')
        elif update.message.text == 'комедия':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='"На деревню дедушке", "Олень", "Плагиатор"')
        elif update.message.text == 'боевик':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='"Джон Уик" все части, "Звёздные воины" "Командо"')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='У меня нет таких жанров!')
    elif mode == 'food':
        if update.message.text == 'сладкое':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='на выбор есть мороженое, блинчики со сгущёнкой, тирамису.')
        elif update.message.text == 'солёное':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='в аасортименте есть солёная рыба с квасом, паста с морепродуктами и пицца пепперони!')
        elif update.message.text == 'острое':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='В меню есть: острая лапша, суп том ям,перчонное мясо утки !(осторожно очень остро! Подаётся с молоком!)! ')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='У меня нет таких вкусов!')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def recommend_film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='какой жанр фильмов предпочитаешь? : ужастик, комедия, боевик.')
    context.user_data['mode'] = 'film'


async def recommend_food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='какой вкус предпочитаешь? : острое, сладкое, солёное.')
    context.user_data['mode'] = 'food'


if __name__ == '__main__':
    load_dotenv()

    bot_token = os.getenv('BOT_TOKEN')

    application = ApplicationBuilder().token(bot_token).build()

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message)

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    guess_the_number_handler = CommandHandler('guess_the_number', guess_the_number)
    recommend_film_handler = CommandHandler('recommend_film', recommend_film)
    recommend_food_handler = CommandHandler('recommend_food', recommend_food)

    application.add_handler(recommend_food_handler)
    application.add_handler(recommend_film_handler)
    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    application.add_handler(guess_the_number_handler)
    application.run_polling()
