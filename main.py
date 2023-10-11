import telebot
import webbrowser
from telebot import types

#подключаемся к нужному нам боту через ранее полученный токен
bot = telebot.TeleBot("6609355269:AAHC-prJEnQMFxz61z3E6ZL7q_TLMS371g4")


#Создадим кнопки, отображающиеся внизу под полем ввода текста
@bot.message_handler(commands=["start"])
def to_start(message):

    '''Кнопки просто будут выводить соответствуюший текст в чат.
    Т.е. нажав "привет" , в чат и вводится слово привет'''

    #создаем кнопки
    markup = types.ReplyKeyboardMarkup()

    button1 = types.KeyboardButton("Привет)")
    markup.row(button1)
    button2 = types.KeyboardButton("Как дела?")
    button3 = types.KeyboardButton("Все ок!")
    button4 = types.KeyboardButton("Давай, пока.")
    markup.row(button2, button3, button4)


    bot.send_message(message.chat.id, f"Hey, {message.from_user.first_name}!", reply_markup=markup)


@bot.message_handler(commands=["talk"])
def lets_talk(message):

    markup = types.ReplyKeyboardMarkup()

    btn1 = types.KeyboardButton('Привет!')
    btn2 = types.KeyboardButton('Пока!')
    btn3 = types.KeyboardButton('Ок')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Как дела?')
    btn5 = types.KeyboardButton('Все ок?')
    btn6 = types.KeyboardButton('Как ты?')
    markup.row(btn4, btn5, btn6)
    btn7 = types.KeyboardButton("Посмотреть кино")
    btn8 = types.KeyboardButton("Посмотреть футбол")
    markup.row(btn7, btn8)
    btn9 = types.KeyboardButton("Получить йогурт")
    btn10 = types.KeyboardButton("Послушать LB")
    markup.row(btn9, btn10)



    bot.send_message(message.chat.id, f"{message.from_user.first_name}, давай поговорим)",
                     reply_markup=markup)

    #чтобы обрабатывать эти кнопки, нам нужно зарегистрировать функцию,
    #которая будет срабатывать при вводе текста
    bot.register_next_step_handler(message, on_click)

def on_click(message):

    if message.text == "Посмотреть кино":
        webbrowser.open("https://rezka.ag/")
    elif message.text == "Посмотреть футбол":
        webbrowser.open("https://myfootball.top/")
    elif message.text == "Получить йогурт":
        # откроем файл с фото
        with open("./yogurt.png", "rb") as file:
            # отправим пользователю фото
            bot.send_photo(message.chat.id, file)
    elif message.text == "Послушать LB":
        with open("./lp_intro.mp3", "rb") as file:
            bot.send_audio(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, "😊")

    #прописываем,чтобы кнопки выполнялись всегда
    bot.register_next_step_handler(message, on_click)


#в первую очередь выполним обработку команды /start
@bot.message_handler(commands = ["main", "hello"])
def main(message):
    """Функция, которая будет вызываться каждый раз,
    когда будет вводиться команда /main , /hello.

    параметр message хранит в себе всю информацию про самого
    пользователя, который работает с ботом и хранит всю
    информацию про сам чат."""

    #каждый раз будем отправлять пользователю слово "Привет!"
    #message.chat.id - это id того чата, с которым мы сейчас взаимодействуем
    bot.send_message(message.chat.id, f"Hey, {message.from_user.first_name}!")

@bot.message_handler(commands=["help"])
def get_help_ingo(message):
    """Функция, выводящая справочную информацию при команде /help"""

    bot.send_message(message.chat.id, "<b>nextBot</b> <em>overall info</em>.", parse_mode="html")  #формат.строка


@bot.message_handler(commands=["user"])
def get_user_info(message):
    """Вывод сообщения про чат или же самого пользователя"""

    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=["site", "website"])
def go_to_site(message):
    """Отправка пользователя на заданный сайт.
    Мы не будем отправлять пользователю никаких сообщений,
    а откроем страницу сайта в браузере"""
    webbrowser.open("https://football.ua/england.html")

@bot.message_handler(content_types=["audio"])
def get_audio(message):
    """Прием  файлов от пользователя (аудио)"""

    #ответим пользователю на отправку изображения
    bot.reply_to(message, "Вау! Красивый голос!")

    # Тут будет реализация кнопок бота

# Кнопки, которые отображаются возле самого сообщения
# пропишем их внутри функции
@bot.message_handler(content_types=["photo"])
def get_photo(message):
    """Прием фото от пользователя и настройка кнопок.
    Без дизайна"""

    #настраиваем кнопки
    #создаем некий объект markup
    markup = types.InlineKeyboardMarkup()

    #добавляем по одной новой кнопке
    #кнопка перехода на сайт rezka
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://rezka.ag/"))
    #кнопка удаления фото
    markup.add(types.InlineKeyboardButton("Удалить фото", callback_data="delete"))
    # кнопка изменения текста
    markup.add(types.InlineKeyboardButton("Изменить текст", callback_data="edit"))

    bot.reply_to(message, f"{message.from_user.first_name}, крутая фотка!", reply_markup = markup)

@bot.message_handler(content_types=["video"])
def get_video(message):

    markup = types.InlineKeyboardMarkup()

    #пропишем все кнопки
    btn_1 = types.InlineKeyboardButton("Перейти на сайт",url = "https://www.youtube.com")
    #создадим строку(первый ряд кнопок в которм будет только одна кнопка)
    markup.row(btn_1)
    #создадим еще две кнопки , но уже для второго ряда
    btn_2 = types.InlineKeyboardButton("Удалить видео", callback_data="delete")
    btn_3 = types.InlineKeyboardButton("Изменить текст", callback_data="edit")
    markup.row(btn_2, btn_3)

    bot.reply_to(message, f"{message.from_user.first_name}, прикольное видео)))", reply_markup=markup)

#создадим функцию, которая будет обрабатывать объект callback_data
@bot.callback_query_handler(func= lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        #для удаления сообщения указываем id чата и id сообщения, которое собираемся удалить
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) #-1 для доступа к предпоследнему сообщению
    elif callback.data == "edit":
        #указываем в качестве аргументов 1-е новый текст и далее то же, что и выше
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def talks(message):
    """Функция, обрабатывающая любой обычный текст, вписанный пользователем,
    а не команду."""

    #выпполним анализ, что вводит пользователь,
    #и в зависимости от его ввода будем выполнять
    #определенные действия. text - это текст,который ввел пользователь
    #приводим текс в нижний регистр для удобства обработки
    if message.text.lower() == "привет)":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nКак дела?")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Все хорошо, а у тебя?")
    elif message.text.lower() == "все ок!" or message.text.lower() == "все норм":
        bot.send_message(message.chat.id, "Это хорошо, рад за тебя.")
    elif message.text.lower() == "пока!" or message.text.lower() == "досвидания!" or message.text.lower() == "давай,пока!":
        bot.send_message(message.chat.id, "Пока)")

    elif message.text.lower() == "id":
        #вернем айдишник пользователя в системе телеграмма
        #reply_to() - будет идти как ответом на предыдущее сообщение от пользователя
        bot.reply_to(message, f"Your ID: {message.from_user.id}")






#нужно сделать, чтобы программа работала бесконечно(постоянно), чтобы бот тоже работал
bot.polling(none_stop=True)

#альтернатива вышепрописанной команде
#bot.infinity_polling()
