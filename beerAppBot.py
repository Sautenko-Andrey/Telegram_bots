import os
import telebot
from telebot import types
from tokens import beer_bot_token as my_token

from beerRNN_executor import ExecutorRNN

from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator, FixedLocator, FormatStrFormatter

bot = telebot.TeleBot(my_token.token)


@bot.message_handler(commands=["start", "hello", "hey", "привет"])
def start_Bot(message):
    """Обработчик команды /start"""

    # пропишем две кнопки поиска
    markup = types.InlineKeyboardMarkup(row_width=2)
    search_by_text_btn = types.InlineKeyboardButton("Пошук за назвою", callback_data="search_by_text")
    search_by_img_btn = types.InlineKeyboardButton("Пошут по фото", callback_data="search_by_img")
    markup.add(search_by_text_btn, search_by_img_btn)

    # поприветствуем пользователя и предложим выбрать способ поиска пива
    bot.send_message(message.chat.id, f"Рад тебе бачити, {message.from_user.first_name} 😁\n"
                                      f"Обери нижче способ пошуку пива (за назвою або по фото)⬇️",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def request_executor(call):
    # получаем способ поиска пива
    mode = call.data

    #respond = "пошук за назвою пива" if mode == "search_by_text" else "пошук пива по фото"

    # отправим подтверждение запроса пользователю
    #bot.send_message(call.message.chat.id, f"Ти обрав {respond} 👍")

    # в зависимости от выбора способа, прдлагаем следующее действие
    if mode == "search_by_text":
        bot.send_message(call.message.chat.id, "Напиши <u>назву пива</u> ↩️", parse_mode="html")
        bot.register_next_step_handler(call.message, rnn_executor)
    elif mode == "search_by_img":
        bot.send_message(call.message.chat.id, "Завантаж <u>фото пива</u> ↩️", parse_mode="html")
        bot.register_next_step_handler(call.message, cnn_executor)
    elif mode == "yes":
        bot.send_message(call.message.chat.id, "Шукаємо ще раз! УРААААА!")
        start_Bot(call.message)
    elif mode == "no":
        bot.send_message(call.message.chat.id, "ОК, побачимось!\n👋")
    else:
        bot.send_message(call.message.chat.id, "Я не розумію, що від мене хочуть)))")



def open_send_img(message, path):
    """Метод открывает и отправляет изображения пользователю"""

    try:
        with open(path, "rb") as file:
            bot.send_photo(message.chat.id, file)
    except Exception as ex:
        print(f"Error while opening beer image: {ex}")


def rnn_executor(message):
    """Рекурентная НС для обработки текста"""

    # получаем запрос пользователя на пиво

    user_beer_request = message.text.strip()

    bot.send_message(message.chat.id, f"Запит на пошук 📍<b>{user_beer_request}</b>📍 прийнят.\nПочинаємо пошук!",
                     parse_mode="html")

    bot.send_message(message.chat.id, "🔎")


    # получаем предсказание от НС (название пива)
    prediction = ExecutorRNN()
    pred_result, pred_img, pred_all_prices = prediction.identify_item(user_beer_request)

    # отправляем ответ пользователю для подтверждения
    # bot.send_message(message.chat.id, f"Ми знайшли твоє пиво!\n"
    #                                   f"Це : {pred_result}")

    # отправляем пользователю картинку с его пивом
    # open_send_img(message,GetBeerData(result).send_data())
    open_send_img(message, pred_img)

    out_of_stock_msg = "<i>немає в наявності</i>"
    curr = " грн"
    bp_msg = " - кращя ціна!"

    prices = [x for x in pred_all_prices.values()]
    best_price = min([x for x in prices if x > 0])

    msg = ("<b><u>💰Ціни у маркетах:</u></b>\n<b>🔺АТБ</b>: " + (
        (str(pred_all_prices['atb']) + curr if pred_all_prices['atb'] > 0 else out_of_stock_msg) if pred_all_prices[
            'atb'] != best_price else f"<b><u>{str(pred_all_prices['atb']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺ЕКО:</b> " + (
               (str(pred_all_prices['eko']) + curr if pred_all_prices['eko'] > 0 else out_of_stock_msg) if
               pred_all_prices['eko'] != best_price else f"<b><u>{str(pred_all_prices['eko']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Varus:</b> " + (
               (str(pred_all_prices['varus']) + curr if pred_all_prices['varus'] > 0 else out_of_stock_msg) if
               pred_all_prices['varus'] != best_price else f"<b><u>{str(pred_all_prices['varus']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Сільпо:</b> " + (
               (str(pred_all_prices['silpo']) + curr if pred_all_prices['silpo'] > 0 else out_of_stock_msg) if
               pred_all_prices['silpo'] != best_price else f"<b><u>{str(pred_all_prices['silpo']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Ашан:</b> " + (
               (str(pred_all_prices['ashan']) + curr if pred_all_prices['ashan'] > 0 else out_of_stock_msg) if
               pred_all_prices['ashan'] != best_price else f"<b><u>{str(pred_all_prices['ashan']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Novus:</b> " + (
               (str(pred_all_prices['novus']) + curr if pred_all_prices['novus'] > 0 else out_of_stock_msg) if
               pred_all_prices['novus'] != best_price else f"<b><u>{str(pred_all_prices['novus']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Metro:</b> " + (
               (str(pred_all_prices['metro']) + curr if pred_all_prices['metro'] > 0 else out_of_stock_msg) if
               pred_all_prices['metro'] != best_price else f"<b><u>{str(pred_all_prices['metro']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Наш Край:</b> " + (
               (str(pred_all_prices['nk']) + curr if pred_all_prices['nk'] > 0 else out_of_stock_msg) if
               pred_all_prices['nk'] != best_price else f"<b><u>{str(pred_all_prices['nk']) + curr + bp_msg}</u></b>")
           + "\n<b>🔺Fozzy:</b> " + (
               (str(pred_all_prices['fozzy']) + curr if pred_all_prices['fozzy'] > 0 else out_of_stock_msg)) if
           pred_all_prices['fozzy'] != best_price else f"<b><u>{str(pred_all_prices['fozzy']) + curr + bp_msg}</u></b>")

    bot.send_message(message.chat.id, msg, parse_mode="html")

    # отправляем пользователю сравнительную диаграмму по ценам на пиво
    markets = ["АТБ", "ЕКО", "Varus", "Сільпо", "Ашан", "Novus", "Metro", "НК", "Fozzy"]

    # create plot
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot()

    colors_diff = []
    for value in prices:

        if value == min([x for x in prices if x > 0]):
            colors_diff.append("red")
        else:
            colors_diff.append("blue")

    ax.bar(markets, prices, color=colors_diff)

    ax.bar(markets, prices, color=colors_diff)
    ax.yaxis.set_major_locator(MaxNLocator(10))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    #ax.legend(["кращя ціна", "ціна"])
    # ax.text(0.05, 0.01, "Червоним виділено кращу ціну")
    plt.title("Ціни у маркетах, грн (червоним виділено кращу ціну!)")
    counter = 0
    plt.savefig(f'compared_prices_{message.from_user.first_name}_{counter}.png')
    open_send_img(message, f'compared_prices_{message.from_user.first_name}_{counter}.png')
    # counter += 1

    # удаляем сгенерированную диаграмму
    try:
        os.remove(f"./compared_prices_{message.from_user.first_name}_{counter}.png")
    except Exception:
        print(f"Error when delete diagram: ./compared_prices_{message.from_user.first_name}_{counter}.png")

    one_more_search(message)


def one_more_search(message):
    '''Еще один поиск'''

    # пропишем две кнопки да или нет
    markup = types.InlineKeyboardMarkup(row_width=2)
    yes_btn = types.InlineKeyboardButton("ТАК", callback_data="yes")
    no_btn = types.InlineKeyboardButton("НІ", callback_data="no")
    markup.add(yes_btn, no_btn)
    bot.send_message(message.chat.id, "Щукаемо ще раз?😊", reply_markup=markup)


def cnn_executor(message):
    """Сверточная НС для обработки фото"""

    bot.send_message(message.chat.id, f"{message.from_user.first_name},вибач, нажаль пошук по фото"
                                      f"тимчасово недоступний.")


@bot.message_handler(content_types=["text", "audio", "video"])
def get_another(message):
    """Обработка других вводов от пользователя"""

    bot.send_message(message.chat.id, "Я не розумію що ти хочешь від мене 😄")
    bot.register_next_step_handler(message, start_Bot)


bot.polling(none_stop=True)
