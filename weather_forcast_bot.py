import telebot
import requests
import json
from tokens import weather_forecast_bot_token as token


bot = telebot.TeleBot(token.token)
API_KEY_OPEN_WEATHER_MAP = "901845bcd5278602fd0633c644c0f2cd"


@bot.message_handler(commands=["start"])
def start(message):
    """Обработчик команды /start.
    """

    # отправляем приветственное сообщение пользователю
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name},"
                                      f" напиши назву міста🏙")



@bot.message_handler(content_types=["text"])
def get_weather(message):
    '''Будем остлеживтаь только введенный пользователь текст (название города)'''

    #получаем название города и присваиваем его переменной
    city = message.text.strip().lower()

    #получаем json с данными по городу
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_OPEN_WEATHER_MAP}&units=metric")

    #проведем проверку на правильность ввода названия города
    if data.status_code != 200:
        bot.send_message(message.chat.id, "Місто вказене невірно!")

    forecast = json.loads(data.text)
    try:
        temperature = forecast['main']['temp']
        humidity = forecast['main']['humidity']
        overall = forecast['weather'][0]['description']
        wind_speed = forecast["wind"]["speed"]
        print(overall)


        #определеямся с небом
        if overall == "scattered clouds":
            sky = "Невелика хмарність"
            #image = "small_cloudy.jpeg"
            image = "🌤"
        elif overall == "overcast clouds":
            sky = "Пасмурно"
            #image = "cloudy.png"
            image = "☁️"
        elif overall == "clear sky":
            sky = "Ясно"
            #image = "sunny.png"
            image = "☀️"
        elif overall == "few clouds":
            sky = "Малооблачно"
            #image = "small_cloudy.jpeg"
            image = "⛅️"
        elif overall == "broken clouds":
            sky = "Розрозрені хмари"
            image = "🌤"
        else:
            sky = "Незрозуміло"
            image = "🤷‍♂️"

        #отпраим ответ пользователю
        bot.reply_to(message, f"<b><i><u>Погода зараз</u></i></b>:\n<b>Температура</b>: {temperature} C\n<b>Вологість</b>: {humidity} %\n"
                              f"<b>Швідкість вітру</b>: {wind_speed} м/с\n<b>Небо</b>: {sky}", parse_mode = "html")


        # with open(f"./weather_pics/{image}", "rb") as file:
        #     bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, image)

    except KeyError:
        print("Ошибка запроса")




bot.polling(none_stop=True)