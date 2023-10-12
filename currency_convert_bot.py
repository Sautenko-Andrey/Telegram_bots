import telebot
from telebot import types
from tokens import currency_convert_bot_token as token

bot = telebot.TeleBot(token.token)
from currency_converter import CurrencyConverter
currency = CurrencyConverter()

money = 0  #плохая идея!

@bot.message_handler(commands=["start"])
def start(message):
    """Обработчик команды /start"""

    #приветственное сообщение для пользователя
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}!\n"
                                      f"Введи сумму ↩️")

    bot.register_next_step_handler(message, executor)

def executor(message):
    """Функция будет срабатывать как только пользователь введет некую сумму."""

    #сумма введенная пользователем
    global money
    try:
        money = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Сумму прописуйте числами 🔢")
        bot.register_next_step_handler(message, executor)
        return  #чтобы последующий код не выполнялся

    if money < 0:
        bot.send_message(message.chat.id, "Сумма повинна бути більше нуля!\nВпишіть сумму")
        bot.register_next_step_handler(message, executor)
        return  # чтобы последующий код не выполнялся


    #создадим набор кнопок
    markup = types.InlineKeyboardMarkup(row_width=2) #в одном ряду будем максимум 2 кнопки
    btn1 = types.InlineKeyboardButton("USD/EUR", callback_data="USD/EUR")
    btn2 = types.InlineKeyboardButton("EUR/USD", callback_data="EUR/USD")
    btn3 = types.InlineKeyboardButton("TRY/USD", callback_data="TRY/USD")
    btn4 = types.InlineKeyboardButton("Інше", callback_data="else")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Оберіть пару для конвертаціі", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "else":
        bot.send_message(call.message.chat.id, "Введіть пару через слеш /")
        bot.register_next_step_handler(call.message, custom_currency)

    #получаем выбранную пару и создаем список к примеру['USD','UAH']
    values = call.data.split('/')

    #производим конвертацию валют
    result = currency.convert(money, values[0], values[1])

    #возвращаем ответ пользователю
    bot.send_message(call.message.chat.id, f"Результат: {round(result,2)} {values[1]}\nПродовжумо конвертацію?\n"
                                           f"Введіть нову сумму")
    bot.register_next_step_handler(call.message, executor)

def custom_currency(message):

    try:
        #получаем данные от пользователя
        values = message.text.upper().split('/')
        # производим конвертацию валют
        result = currency.convert(money, values[0], values[1])

        # возвращаем ответ пользователю
        bot.send_message(message.chat.id, f"Результат: {round(result, 2)} {values[1]}\nПродовжумо конвертацію?\n"
                                               f"Введіть нову сумму")
        bot.register_next_step_handler(message, executor)
    except Exception:
        # возвращаем ответ пользователю в случае возникновения хоть какой-либо ошибки
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, ти надав некоректні данні...😔\n"
                                          f"Спробуй ще раз 😊")
        bot.register_next_step_handler(message, custom_currency)



bot.polling(none_stop=True)