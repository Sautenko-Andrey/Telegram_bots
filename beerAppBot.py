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
                                      f"Обери нижче способ пошуку пива (за назвою або по фото)",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def request_executor(call):

    #получаем способ поиска пива
    mode = call.data

    respond = "пошук за назвою пива" if mode == "search_by_text" else "пошук пива по фото"

    #отправим подтверждение запроса пользователю
    bot.send_message(call.message.chat.id, f"Ти обрав {respond} 👍")

    #в зависимости от выбора способа, прдлагаем следующее действие
    if mode == "search_by_text":
        bot.send_message(call.message.chat.id, "Напиши назву пива")
        bot.register_next_step_handler(call.message, rnn_executor)
    else:
        bot.send_message(call.message.chat.id, "Завантаж фото пива")
        bot.register_next_step_handler(call.message, cnn_executor)


def open_send_img(message, path):
    """Метод открывает и отправляет изображения пользователю"""

    with open(path, "rb") as file:
        bot.send_photo(message.chat.id, file)


def rnn_executor(message):
    """Рекурентная НС для обработки текста"""

    #получаем запрос пользователя на пиво

    user_beer_request = message.text.strip()

    bot.send_message(message.chat.id, f"Запит на пошук 📍{user_beer_request}📍 прийнят. Починаємо пошук!")

    #получаем предсказание от НС (название пива)
    prediction = ExecutorRNN()
    pred_result, pred_img ,pred_all_prices = prediction.identify_item(user_beer_request)

    #отправляем ответ пользователю для подтверждения
    bot.send_message(message.chat.id, f"Ми знайшли твоє пиво!\n"
                                      f"Це : {pred_result}")

    #отправляем пользователю картинку с его пивом
    #open_send_img(message,GetBeerData(result).send_data())
    open_send_img(message, pred_img)

    #если цена 0, указываем, что пива нет в наличии в маркете
    #pred_all_prices = {key:'нет в наличии' for key, value in pred_all_prices.items if value == 0}

    # #меняем значение 0 на "нет в наличии"
    for key, value in pred_all_prices.items():
        if value == 0:
            value = "нет в наличии"

    #отправляем пользователю все цены
    bot.send_message(message.chat.id, f"Цены в супермаркетах:\n"
                                      f"---------------------\n"
                                      f"АТБ: {pred_all_prices['atb']} грн\n"
                                      f"ЕКО: {pred_all_prices['eko']} грн\n"
                                      f"Varus: {pred_all_prices['varus']} грн\n"
                                      f"Сільпо: {pred_all_prices['silpo']} грн\n"
                                      f"Ашан: {pred_all_prices['ashan']} грн\n"
                                      f"Novus: {pred_all_prices['novus']} грн\n"
                                      f"Metro: {pred_all_prices['metro']} грн\n"
                                      f"Наш Край: {pred_all_prices['nk']} грн\n"
                                      f"Fozzy: {pred_all_prices['fozzy']} грн")

    #отправляем пользователю сравнительную диаграмму по ценам на пиво
    markets = ["АТБ", "ЕКО", "Varus", "Сільпо", "Ашан", "Novus", "Metro", "НК", "Fozzy"]
    prices = [x for x in pred_all_prices.values()]
    #prices = pred_all_prices

    market_colors = ['blue', 'orange', 'green',
                     'red', 'purple', 'brown',
                     'pink', 'grey', 'olive']

    # create plot
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    ax.bar(markets, (prices), color=market_colors)
    ax.yaxis.set_major_locator(MaxNLocator(10))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    plt.title("Ціни у маркетах, грн")
    counter = 0
    plt.savefig(f'compared_prices_{message.from_user.first_name}_{counter}.png')
    open_send_img(message, f'compared_prices_{message.from_user.first_name}_{counter}.png')
    counter +=1





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
