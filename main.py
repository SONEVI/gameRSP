import telebot
import random

# Создаем экземпляр бота
bot = telebot.TeleBot('5903454038:AAEcqkMicwlWd7-u84fNb3LlyTgTMbqSSME')

user = {'total_games': 0,
        'wins': 0}

i = '🗿', '✂', '📜', '🦎', '🖖'


def get_random_word():
    return random.choice(i)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Давай!", "Не хочу!")
    bot.send_message(m.chat.id, 'Приветствую в игре "Камень-ножницы-бумага". Не хочешь сыграть со мной?'
                                ' Выбери:\nДАВАЙ, если готов сыграть.\nНЕ ХОЧУ, если не хочешь играть.',
                     reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_message(m.chat.id, 'Правила игры таковы:\nЭто простая игра, в которую играют по всему миру с множеством '
                                'разных названий и вариантов. Это хороший способ, чтобы решить, чья очередь наступает, '
                                'чтобы сделать что-то, и это разыгрывается на конкурентной основе. Ножницы режут '
                                'бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в '
                                'то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, '
                                'которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, '
                                'разумеется, затупляет ножницы. .\nЯ рандомно выбираю один '
                                'из предметов, а вы, в свою очередь, должны выбрать предмет на клавиатуре.\nЕсли я '
                                'отправляю вам "Камень", а вы мне "Ножницы", непосредственно я выигрываю. А если вы '
                                'мне отправите "Бумага", а я вам "Камень", победили вы.')
    image = open(f'knb_photo.jpg')
    image.close()
    bot.send_photo(m.chat.id, image)


@bot.message_handler(commands=["stat"])
def stat(m, res=False):
    bot.send_message(m.chat.id, 'Всего игр сыграно: ' + str(user["total_games"]) +
                     '\nИгр выиграно: ' + str(user["wins"]))


@bot.message_handler(content_types=["text"])
def handle_text(m):
    if m.text in ['Давай!']:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🗿', '✂', '📜')
        bot.send_message(m.chat.id, 'Отлично! Выбери на своей клавиатуре выбор ответа.', reply_markup=markup)
    elif m.text in ['🗿', '✂', '📜']:
        user['total_games'] += 1
        bot_choice = random.choice(i)
        bot.send_message(m.chat.id, bot_choice)
        if bot_choice == '🗿':
            if m.text == '✂' or spok:
                bot.send_message(m.chat.id, 'Вы проиграли. Победа за мной.')
            elif m.text == '🗿':
                bot.send_message(m.chat.id, 'У нас ничья. Вам повезло.')
            elif m.text == '📜' or kamen:
                bot.send_message(m.chat.id, 'Вы выиграли. Мои поздравления.')
                user['wins'] += 1
        elif bot_choice == '📜':
            if m.text == '✂':
                bot.send_message(m.chat.id, 'Вы выиграли. Мои поздравления.')
                user['wins'] += 1
            elif m.text == '🗿':
                bot.send_message(m.chat.id, 'Вы проиграли. Победа за мной.')
            elif m.text == '📜':
                bot.send_message(m.chat.id, 'У нас ничья. Вам повезло.')
        elif bot_choice == '✂':
            if m.text == '🗿':
                bot.send_message(m.chat.id, 'Вы выиграли. Мои поздравления.')
                user['wins'] += 1
            elif m.text == '📜':
                bot.send_message(m.chat.id, 'Вы проиграли. Победа за мной.')
            elif m.text == '✂':
                bot.send_message(m.chat.id, 'У нас ничья. Вам повезло.')
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row("Давай!", "Не хочу.")
        bot.send_message(m.chat.id, 'Отличная игра. Не хочешь сыграть еще раз?', reply_markup=markup)
    elif m.text in ['Не хочу.']:
        bot.send_message(m.chat.id, 'Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!"')
    else:
        bot.send_message(m.chat.id, 'Я тебя не понимаю. Я реагирую только на:'
                                    '\n- варианты ответа.\n- команды /help и /stat.')


bot.polling(none_stop=True, interval=0)
