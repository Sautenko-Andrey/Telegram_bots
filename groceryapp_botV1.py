import telebot
from telebot import types
from tokens import grocery_appV1 as my_token
import time

bot = telebot.TeleBot(my_token.token)


@bot.message_handler(commands=["start"])
def start(message):
    """Метод, обрабатывающий команду /start"""

    # получаем название продукта
    bot.send_message(message.chat.id, f"Вітаю, {message.from_user.first_name}👋\n"
                                      f"Будь ласка введіть назву продукта🛒")

    bot.register_next_step_handler(message, get_item_name)


def rnn_searcher(message, item_name:str) -> str:
    """Метод для распознования запроса пользователя(товара)
    при помощи НС."""

    bot.send_message(message.chat.id, "Шукаю продукт...👀")
    time.sleep(1)
    bot.send_message(message.chat.id, "Трошки почекайте 🙏")
    time.sleep(2)
    return item_name



def get_item_name(message) -> str:
    """Функция будет считывать название продукта и искать его в БД"""

    #получаем запрос пользователя
    item = message.text.strip().lower()

    #имитация работы нейронной сети, которая будет определять какой товар ищет пользователь
    item = rnn_searcher(message,item)

    #подтвердим пользователю его запрос
    bot.send_message(message.chat.id, f'Ви шукаєте "{item}"')

    #регистрируем и вызываем следующую функцию для получения города
    bot.send_message(message.chat.id, f"Будь ласка вкажіть ваше місто, де будемо шукати🛒")
    bot.register_next_step_handler(message, get_city)

    return item

def get_city(message) -> str:
    """Считывание города пользователя"""

    city = message.text.strip().lower()

    # подтвердим пользователю его город
    bot.send_message(message.chat.id, f'Ви у місті {city[0].upper() + city[1:]}')


    # создадим набор кнопок
    markup = types.InlineKeyboardMarkup(row_width=3)  # в одном ряду будем максимум 2 кнопки
    atb = types.InlineKeyboardButton("АТБ", callback_data="ATB")
    eko = types.InlineKeyboardButton("ЕКО", callback_data="EKO")
    varus = types.InlineKeyboardButton("Varus", callback_data="Varus")
    silpo = types.InlineKeyboardButton("Сільпо", callback_data="Silpo")
    ashan = types.InlineKeyboardButton("Ашан", callback_data="Ashan")
    novus = types.InlineKeyboardButton("Novus", callback_data="Novus")
    metro = types.InlineKeyboardButton("Metro", callback_data="Metro")
    nk = types.InlineKeyboardButton("Наш Край", callback_data="NK")
    fozzy = types.InlineKeyboardButton("Fozzy", callback_data="Fozzy")
    markup.add(atb, eko, varus, silpo, ashan, novus, metro, nk, fozzy)

    bot.send_message(message.chat.id, "Оберіть маркет", reply_markup=markup)

    # регистрируем и вызываем следующую функцию для выбора маркетов
    #bot.register_next_step_handler(message, get_markets)

    return city

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    market = call.data
    bot.send_message(call.message.chat.id, f"Ти обрав {market}")




bot.polling(none_stop=True)
