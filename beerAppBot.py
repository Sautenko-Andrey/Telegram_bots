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

    #выполним проверку способа поиска
    # if mode != "search_by_text" and mode != "search_by_img":
    #     bot.send_message(call.message.chat.id, "Оберіть способ пошуку, натиснувши одну з двох кнопок")
    #     bot.register_next_step_handler(call.message, start_Bot)


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



def rnn_executor(message):
    """Рекурентная НС для обработки текста"""

    #получаем запрос пользователя на пиво
    user_beer_request = message.text.strip()

    bot.send_message(message.chat.id, f"Запит на пошук 📍{user_beer_request}📍 прийнят. Починаємо пошук!")

    #получаем предсказание от НС (название пива)
    prediction = ExecutorRNN()
    result = prediction.identify_item(user_beer_request)

    #отправляем ответ пользователю для подтверждения
    bot.send_message(message.chat.id, f"Ми знайшли твоє пиво!\n"
                                      f"Це : {result}")

    #отправляем пользователю картинку с его пивом
    if result == "Пиво 5.0 Original Lager светлое 0.5 в ж.б":
        with open("../beerBot_DATA/pics/beer_5_0_original_lager__svitle_0_5_l_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво 5.0 Original pills светлое 0,5 л в банке":
        with open("../beerBot_DATA/pics/5_0_original_pils_svitle_0_5_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке":
        with open("../beerBot_DATA/pics/5_0_original_weiss_beer_0_5_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке":
        with open("../beerBot_DATA/pics/5_0_original_craft_0_5_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво amstel светлое 0,5 л в бутылке":
        with open("../beerBot_DATA/pics/amstel_svitle_0_5_glass.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво amstel светлое 0,5 л в банке":
        with open("../beerBot_DATA/pics/amstel_svitle_0_5_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво арсенал крепкое 0,5 л в бутылке":
        with open("../beerBot_DATA/pics/arsenal_micne_05_glass.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво арсенал крепкое светлое 2 л в бутылке":
        with open("../beerBot_DATA/pics/arsenal_micne_2L_pl.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке":
        with open("../beerBot_DATA/pics/bavaria_granat_bezalk_svetl_05jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
    elif result == "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке":
        with open("../beerBot_DATA/pics/bavaria_liquid_apple_svitle_bezalk_05_jb.png", "rb") as file:
            bot.send_photo(message.chat.id, file)





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
