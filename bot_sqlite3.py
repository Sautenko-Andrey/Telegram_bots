import telebot
import sqlite3

bot = telebot.TeleBot("6537821050:AAHw0CtcSx4U7AVRZJrLfLx5ivqOT8VLCW0")
name = None

@bot.message_handler(commands=["start"])
def start_method(message):
    '''Создадим обработчик команды /start.
    Когда пользователь будет запускать наш бот, мы будем создавать саму базу данных,
    а так же в БД будем создавать новую табличку, в которой мы будем хранить всех наших пользователей.'''

    #выполним создание самой БД
    connection = sqlite3.connect("saut.sql")  #создаем файл saut.sql в котром будет храниться БД

    #создадим объект, через которой сможет выполнять команды БД
    cursor = connection.cursor()

    #создадим новую таблицу в БД .
    #В нее в последствии будем записывать пользователей
    #будут созданы поля: id, имя и пароль
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,"
                   "name varchar(50), password varchar(50))")

    #создаем таблицу
    connection.commit()

    #закрываем БД
    cursor.close()
    #закрываем соединение
    connection.close()

    #выведем сообщение пользователю
    bot.send_message(message.chat.id, "Привет! Сейчас тебя зарегистрируем,"
                                      "пожалуйста введи свое имя")

    #зарегистрируем следующую функцию,которая у нас должна срабатывать
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    '''В этой функции получаем тот текст, который вводит пользователь,
    и этот текс мы будем записывать в переменную name'''
    global name
    name = message.text.strip()   #удалим все возможные пробелы до и после текста

    #далее попросим пользователяввести пароль
    bot.send_message(message.chat.id, "Введи пароль")
    bot.register_next_step_handler(message, get_password)

def get_password(message):
    '''В этой функции получаем тот текст, которыйвводит пользователь,
    и этот текс мы будем записывать в переменную password'''

    password = message.text.strip()   #удалим все возможные пробелы до и после текста

    #далее мы должны зарегистрировать пользователя по его имени и паролю,
    #которые мы получили
    #подключение и закрытие БД
    connection = sqlite3.connect("saut.sql")  # создаем файл saut.sql в котром будет храниться БД
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    connection.commit()
    cursor.close()
    connection.close()


    #отобразим кнопку "Список пользователей"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Список пользователей",
                                                  callback_data="users_data"))
    bot.send_message(message.chat.id, "Пользователь успешно зарегистрирован.",
                     reply_markup=markup)  # reply_markup=markup - кнопка будет выведена вместе с сообщением


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    """Обработчик кнопки 'Список пользователей'"""
    # подключение и закрытие БД
    connection = sqlite3.connect("saut.sql")  # создаем файл saut.sql в котром будет храниться БД
    cursor = connection.cursor()
    #выбираем все поля из таблицы
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()  #эта функция вернет нам полностью все найденные записи

    #далее переберем все полученные данные и выведем их на экран
    info = ''
    for el in users:
        info += f"Имя: {el[1]}, пароль: {el[2]}\n"

    cursor.close()
    connection.close()

    #передаем созданную строку пользователю
    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)