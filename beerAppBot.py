import telebot
from telebot import types
from tokens import beer_bot_token as my_token

from beerRNN_executor import ExecutorRNN

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
    pred_result, pred_img = prediction.identify_item(user_beer_request)

    #отправляем ответ пользователю для подтверждения
    bot.send_message(message.chat.id, f"Ми знайшли твоє пиво!\n"
                                      f"Це : {pred_result}")

    #отправляем пользователю картинку с его пивом
    #open_send_img(message,GetBeerData(result).send_data())
    open_send_img(message, pred_img)



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
