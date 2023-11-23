import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model

from beer_bot_utils import *


import pymongo


class ExecutorRNN:
    # установим соединение с Mongo DB
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")

    # подключаемся к БД
    current_db = db_client["products_db"]

    # создаем коллекцию beers
    beer_collection = current_db["beers"]

    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    # получаем доступ к папке с текстовыми файлами
    path = "../beerBot_DATA/all_beers"
    texts_dir = os.listdir(path)

    def prepearing_data(self):
        '''Подготавливаем текст'''
        get_text_data = RefersForRNN()
        texts = get_text_data.get_text_from_DB()[0]
        return texts

    def create_tokenizer(self):
        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(self.prepearing_data())
        return tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = dict(map(reversed, self.create_tokenizer().word_index.items()))
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def identify_item(self, user_text):

        # загружаем обученную модель НС для распознования товара по тексту:
        model = load_model("./beer_bot_model_text")

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.create_tokenizer()

        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        result = model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')
        if np.argmax(result) == 0:
            return (self.beer_collection.find_one({"id": 0})["name"], self.beer_collection.find_one({"id": 0})["img"],
                    self.beer_collection.find_one({"id": 0})["prices"])
        elif np.argmax(result) == 1:
            return (self.beer_collection.find_one({"id": 1})["name"], self.beer_collection.find_one({"id": 1})["img"],
                    self.beer_collection.find_one({"id": 1})["prices"])
        elif np.argmax(result) == 2:
            return (self.beer_collection.find_one({"id": 2})["name"], self.beer_collection.find_one({"id": 2})["img"],
                    self.beer_collection.find_one({"id": 2})["prices"])
        elif np.argmax(result) == 3:
            return (self.beer_collection.find_one({"id": 3})["name"], self.beer_collection.find_one({"id": 3})["img"],
                    self.beer_collection.find_one({"id": 3})["prices"])
        elif np.argmax(result) == 4:
            return (self.beer_collection.find_one({"id": 4})["name"], self.beer_collection.find_one({"id": 4})["img"],
                    self.beer_collection.find_one({"id": 4})["prices"])
        elif np.argmax(result) == 5:
            return (self.beer_collection.find_one({"id": 5})["name"], self.beer_collection.find_one({"id": 5})["img"],
                    self.beer_collection.find_one({"id": 5})["prices"])
        if np.argmax(result) == 6:
            return (self.beer_collection.find_one({"id": 6})["name"], self.beer_collection.find_one({"id": 6})["img"],
                    self.beer_collection.find_one({"id": 6})["prices"])
        elif np.argmax(result) == 7:
            return (self.beer_collection.find_one({"id": 7})["name"], self.beer_collection.find_one({"id": 7})["img"],
                    self.beer_collection.find_one({"id": 7})["prices"])
        elif np.argmax(result) == 8:
            return (self.beer_collection.find_one({"id": 8})["name"], self.beer_collection.find_one({"id": 8})["img"],
                    self.beer_collection.find_one({"id": 8})["prices"])
        elif np.argmax(result) == 9:
            return (self.beer_collection.find_one({"id": 9})["name"], self.beer_collection.find_one({"id": 9})["img"],
                    self.beer_collection.find_one({"id": 9})["prices"])
        elif np.argmax(result) == 10:
            return (self.beer_collection.find_one({"id": 10})["name"], self.beer_collection.find_one({"id": 10})["img"],
                    self.beer_collection.find_one({"id": 10})["prices"])
        elif np.argmax(result) == 11:
            return (self.beer_collection.find_one({"id": 11})["name"], self.beer_collection.find_one({"id": 11})["img"],
                    self.beer_collection.find_one({"id": 11})["prices"])
        elif np.argmax(result) == 12:
            return (self.beer_collection.find_one({"id": 12})["name"], self.beer_collection.find_one({"id": 12})["img"],
                    self.beer_collection.find_one({"id": 12})["prices"])
        elif np.argmax(result) == 13:
            return (self.beer_collection.find_one({"id": 13})["name"], self.beer_collection.find_one({"id": 13})["img"],
                    self.beer_collection.find_one({"id": 13})["prices"])
        elif np.argmax(result) == 14:
            return (self.beer_collection.find_one({"id": 14})["name"], self.beer_collection.find_one({"id": 14})["img"],
                    self.beer_collection.find_one({"id": 14})["prices"])
        elif np.argmax(result) == 15:
            return (self.beer_collection.find_one({"id": 15})["name"], self.beer_collection.find_one({"id": 15})["img"],
                    self.beer_collection.find_one({"id": 15})["prices"])
        elif np.argmax(result) == 16:
            return (self.beer_collection.find_one({"id": 16})["name"], self.beer_collection.find_one({"id": 16})["img"],
                    self.beer_collection.find_one({"id": 16})["prices"])
        elif np.argmax(result) == 17:
            return (self.beer_collection.find_one({"id": 17})["name"], self.beer_collection.find_one({"id": 17})["img"],
                    self.beer_collection.find_one({"id": 17})["prices"])
        elif np.argmax(result) == 18:
            return (self.beer_collection.find_one({"id": 18})["name"], self.beer_collection.find_one({"id": 18})["img"],
                    self.beer_collection.find_one({"id": 18})["prices"])
        elif np.argmax(result) == 19:
            return (self.beer_collection.find_one({"id": 19})["name"], self.beer_collection.find_one({"id": 19})["img"],
                    self.beer_collection.find_one({"id": 19})["prices"])
        elif np.argmax(result) == 20:
            return (self.beer_collection.find_one({"id": 20})["name"], self.beer_collection.find_one({"id": 20})["img"],
                    self.beer_collection.find_one({"id": 20})["prices"])
        elif np.argmax(result) == 21:
            return (self.beer_collection.find_one({"id": 21})["name"], self.beer_collection.find_one({"id": 21})["img"],
                    self.beer_collection.find_one({"id": 21})["prices"])
        elif np.argmax(result) == 22:
            return (self.beer_collection.find_one({"id": 22})["name"], self.beer_collection.find_one({"id": 22})["img"],
                    self.beer_collection.find_one({"id": 22})["prices"])
        elif np.argmax(result) == 23:
            return (self.beer_collection.find_one({"id": 23})["name"], self.beer_collection.find_one({"id": 23})["img"],
                    self.beer_collection.find_one({"id": 23})["prices"])
        elif np.argmax(result) == 24:
            return (self.beer_collection.find_one({"id": 24})["name"], self.beer_collection.find_one({"id": 24})["img"],
                    self.beer_collection.find_one({"id": 24})["prices"])
        elif np.argmax(result) == 25:
            return (self.beer_collection.find_one({"id": 25})["name"], self.beer_collection.find_one({"id": 25})["img"],
                    self.beer_collection.find_one({"id": 25})["prices"])
        elif np.argmax(result) == 26:
            return (self.beer_collection.find_one({"id": 26})["name"], self.beer_collection.find_one({"id": 26})["img"],
                    self.beer_collection.find_one({"id": 26})["prices"])
        elif np.argmax(result) == 27:
            return (self.beer_collection.find_one({"id": 27})["name"], self.beer_collection.find_one({"id": 27})["img"],
                    self.beer_collection.find_one({"id": 27})["prices"])
        elif np.argmax(result) == 28:
            return (self.beer_collection.find_one({"id": 28})["name"], self.beer_collection.find_one({"id": 28})["img"],
                    self.beer_collection.find_one({"id": 28})["prices"])
        elif np.argmax(result) == 29:
            return (self.beer_collection.find_one({"id": 29})["name"], self.beer_collection.find_one({"id": 29})["img"],
                    self.beer_collection.find_one({"id": 29})["prices"])
        elif np.argmax(result) == 30:
            return (self.beer_collection.find_one({"id": 30})["name"], self.beer_collection.find_one({"id": 30})["img"],
                    self.beer_collection.find_one({"id": 30})["prices"])
        elif np.argmax(result) == 31:
            return (self.beer_collection.find_one({"id": 31})["name"], self.beer_collection.find_one({"id": 31})["img"],
                    self.beer_collection.find_one({"id": 31})["prices"])
        elif np.argmax(result) == 32:
            return (self.beer_collection.find_one({"id": 32})["name"], self.beer_collection.find_one({"id": 32})["img"],
                    self.beer_collection.find_one({"id": 32})["prices"])
        elif np.argmax(result) == 33:
            return (self.beer_collection.find_one({"id": 33})["name"], self.beer_collection.find_one({"id": 33})["img"],
                    self.beer_collection.find_one({"id": 33})["prices"])
        elif np.argmax(result) == 34:
            return (self.beer_collection.find_one({"id": 34})["name"], self.beer_collection.find_one({"id": 34})["img"],
                    self.beer_collection.find_one({"id": 34})["prices"])
        elif np.argmax(result) == 35:
            return (self.beer_collection.find_one({"id": 35})["name"], self.beer_collection.find_one({"id": 35})["img"],
                    self.beer_collection.find_one({"id": 35})["prices"])
        elif np.argmax(result) == 36:
            return (self.beer_collection.find_one({"id": 36})["name"], self.beer_collection.find_one({"id": 36})["img"],
                    self.beer_collection.find_one({"id": 36})["prices"])
        elif np.argmax(result) == 37:
            return (self.beer_collection.find_one({"id": 37})["name"], self.beer_collection.find_one({"id": 37})["img"],
                    self.beer_collection.find_one({"id": 37})["prices"])
        elif np.argmax(result) == 38:
            return (self.beer_collection.find_one({"id": 38})["name"], self.beer_collection.find_one({"id": 38})["img"],
                    self.beer_collection.find_one({"id": 38})["prices"])
        elif np.argmax(result) == 39:
            return (self.beer_collection.find_one({"id": 39})["name"], self.beer_collection.find_one({"id": 39})["img"],
                    self.beer_collection.find_one({"id": 39})["prices"])
        elif np.argmax(result) == 40:
            return (self.beer_collection.find_one({"id": 40})["name"], self.beer_collection.find_one({"id": 40})["img"],
                    self.beer_collection.find_one({"id": 40})["prices"])
        elif np.argmax(result) == 41:
            return (self.beer_collection.find_one({"id": 41})["name"], self.beer_collection.find_one({"id": 41})["img"],
                    self.beer_collection.find_one({"id": 41})["prices"])
        elif np.argmax(result) == 42:
            return (self.beer_collection.find_one({"id": 42})["name"], self.beer_collection.find_one({"id": 42})["img"],
                    self.beer_collection.find_one({"id": 42})["prices"])
        elif np.argmax(result) == 43:
            return (self.beer_collection.find_one({"id": 43})["name"], self.beer_collection.find_one({"id": 43})["img"],
                    self.beer_collection.find_one({"id": 43})["prices"])
        elif np.argmax(result) == 44:
            return (self.beer_collection.find_one({"id": 44})["name"], self.beer_collection.find_one({"id": 44})["img"],
                    self.beer_collection.find_one({"id": 44})["prices"])
        elif np.argmax(result) == 45:
            return (self.beer_collection.find_one({"id": 45})["name"], self.beer_collection.find_one({"id": 45})["img"],
                    self.beer_collection.find_one({"id": 45})["prices"])
        elif np.argmax(result) == 46:
            return (self.beer_collection.find_one({"id": 46})["name"], self.beer_collection.find_one({"id": 46})["img"],
                    self.beer_collection.find_one({"id": 46})["prices"])
        elif np.argmax(result) == 47:
            return (self.beer_collection.find_one({"id": 47})["name"], self.beer_collection.find_one({"id": 47})["img"],
                    self.beer_collection.find_one({"id": 47})["prices"])
        elif np.argmax(result) == 48:
            return (self.beer_collection.find_one({"id": 48})["name"], self.beer_collection.find_one({"id": 48})["img"],
                    self.beer_collection.find_one({"id": 48})["prices"])
        elif np.argmax(result) == 49:
            return (self.beer_collection.find_one({"id": 49})["name"], self.beer_collection.find_one({"id": 49})["img"],
                    self.beer_collection.find_one({"id": 49})["prices"])
        elif np.argmax(result) == 50:
            return (self.beer_collection.find_one({"id": 50})["name"], self.beer_collection.find_one({"id": 50})["img"],
                    self.beer_collection.find_one({"id": 50})["prices"])
        elif np.argmax(result) == 51:
            return (self.beer_collection.find_one({"id": 51})["name"], self.beer_collection.find_one({"id": 51})["img"],
                    self.beer_collection.find_one({"id": 51})["prices"])
        elif np.argmax(result) == 52:
            return (self.beer_collection.find_one({"id": 52})["name"], self.beer_collection.find_one({"id": 52})["img"],
                    self.beer_collection.find_one({"id": 52})["prices"])
        elif np.argmax(result) == 53:
            return (self.beer_collection.find_one({"id": 53})["name"], self.beer_collection.find_one({"id": 53})["img"],
                    self.beer_collection.find_one({"id": 53})["prices"])
        elif np.argmax(result) == 54:
            return (self.beer_collection.find_one({"id": 54})["name"], self.beer_collection.find_one({"id": 54})["img"],
                    self.beer_collection.find_one({"id": 54})["prices"])
        elif np.argmax(result) == 55:
            return (self.beer_collection.find_one({"id": 55})["name"], self.beer_collection.find_one({"id": 55})["img"],
                    self.beer_collection.find_one({"id": 55})["prices"])
        elif np.argmax(result) == 56:
            return (self.beer_collection.find_one({"id": 56})["name"], self.beer_collection.find_one({"id": 56})["img"],
                    self.beer_collection.find_one({"id": 56})["prices"])
        elif np.argmax(result) == 57:
            return (self.beer_collection.find_one({"id": 57})["name"], self.beer_collection.find_one({"id": 57})["img"],
                    self.beer_collection.find_one({"id": 57})["prices"])
        elif np.argmax(result) == 58:
            return (self.beer_collection.find_one({"id": 58})["name"], self.beer_collection.find_one({"id": 58})["img"],
                    self.beer_collection.find_one({"id": 58})["prices"])
        elif np.argmax(result) == 59:
            return (self.beer_collection.find_one({"id": 59})["name"], self.beer_collection.find_one({"id": 59})["img"],
                    self.beer_collection.find_one({"id": 59})["prices"])
        elif np.argmax(result) == 60:
            return (self.beer_collection.find_one({"id": 60})["name"], self.beer_collection.find_one({"id": 60})["img"],
                    self.beer_collection.find_one({"id": 60})["prices"])
        elif np.argmax(result) == 61:
            return (self.beer_collection.find_one({"id": 61})["name"], self.beer_collection.find_one({"id": 61})["img"],
                    self.beer_collection.find_one({"id": 61})["prices"])
        elif np.argmax(result) == 62:
            return (self.beer_collection.find_one({"id": 62})["name"], self.beer_collection.find_one({"id": 62})["img"],
                    self.beer_collection.find_one({"id": 62})["prices"])
        elif np.argmax(result) == 63:
            return (self.beer_collection.find_one({"id": 63})["name"], self.beer_collection.find_one({"id": 63})["img"],
                    self.beer_collection.find_one({"id": 63})["prices"])
        elif np.argmax(result) == 64:
            return (self.beer_collection.find_one({"id": 64})["name"], self.beer_collection.find_one({"id": 64})["img"],
                    self.beer_collection.find_one({"id": 64})["prices"])
        elif np.argmax(result) == 65:
            return (self.beer_collection.find_one({"id": 65})["name"], self.beer_collection.find_one({"id": 65})["img"],
                    self.beer_collection.find_one({"id": 65})["prices"])
        elif np.argmax(result) == 66:
            return (self.beer_collection.find_one({"id": 66})["name"], self.beer_collection.find_one({"id": 66})["img"],
                    self.beer_collection.find_one({"id": 66})["prices"])
        elif np.argmax(result) == 67:
            return (self.beer_collection.find_one({"id": 67})["name"], self.beer_collection.find_one({"id": 67})["img"],
                    self.beer_collection.find_one({"id": 67})["prices"])
        elif np.argmax(result) == 68:
            return (self.beer_collection.find_one({"id": 68})["name"], self.beer_collection.find_one({"id": 68})["img"],
                    self.beer_collection.find_one({"id": 68})["prices"])
        elif np.argmax(result) == 69:
            return (self.beer_collection.find_one({"id": 69})["name"], self.beer_collection.find_one({"id": 69})["img"],
                    self.beer_collection.find_one({"id": 69})["prices"])
        elif np.argmax(result) == 70:
            return (self.beer_collection.find_one({"id": 70})["name"], self.beer_collection.find_one({"id": 70})["img"],
                    self.beer_collection.find_one({"id": 70})["prices"])
        elif np.argmax(result) == 71:
            return (self.beer_collection.find_one({"id": 71})["name"], self.beer_collection.find_one({"id": 71})["img"],
                    self.beer_collection.find_one({"id": 71})["prices"])
        elif np.argmax(result) == 72:
            return (self.beer_collection.find_one({"id": 72})["name"], self.beer_collection.find_one({"id": 72})["img"],
                    self.beer_collection.find_one({"id": 72})["prices"])
        elif np.argmax(result) == 73:
            return (self.beer_collection.find_one({"id": 73})["name"], self.beer_collection.find_one({"id": 73})["img"],
                    self.beer_collection.find_one({"id": 73})["prices"])
        elif np.argmax(result) == 74:
            return (self.beer_collection.find_one({"id": 74})["name"], self.beer_collection.find_one({"id": 74})["img"],
                    self.beer_collection.find_one({"id": 74})["prices"])
        elif np.argmax(result) == 75:
            return (self.beer_collection.find_one({"id": 75})["name"], self.beer_collection.find_one({"id": 75})["img"],
                    self.beer_collection.find_one({"id": 75})["prices"])
        elif np.argmax(result) == 76:
            return (self.beer_collection.find_one({"id": 76})["name"], self.beer_collection.find_one({"id": 76})["img"],
                    self.beer_collection.find_one({"id": 76})["prices"])
        elif np.argmax(result) == 77:
            return (self.beer_collection.find_one({"id": 77})["name"], self.beer_collection.find_one({"id": 77})["img"],
                    self.beer_collection.find_one({"id": 77})["prices"])
        elif np.argmax(result) == 78:
            return (self.beer_collection.find_one({"id": 78})["name"], self.beer_collection.find_one({"id": 78})["img"],
                    self.beer_collection.find_one({"id": 78})["prices"])
        elif np.argmax(result) == 79:
            return (self.beer_collection.find_one({"id": 79})["name"], self.beer_collection.find_one({"id": 79})["img"],
                    self.beer_collection.find_one({"id": 79})["prices"])
        elif np.argmax(result) == 80:
            return (self.beer_collection.find_one({"id": 80})["name"], self.beer_collection.find_one({"id": 80})["img"],
                    self.beer_collection.find_one({"id": 80})["prices"])
        elif np.argmax(result) == 81:
            return (self.beer_collection.find_one({"id": 81})["name"], self.beer_collection.find_one({"id": 81})["img"],
                    self.beer_collection.find_one({"id": 81})["prices"])
        elif np.argmax(result) == 82:
            return (self.beer_collection.find_one({"id": 82})["name"], self.beer_collection.find_one({"id": 82})["img"],
                    self.beer_collection.find_one({"id": 82})["prices"])
        elif np.argmax(result) == 83:
            return (self.beer_collection.find_one({"id": 83})["name"], self.beer_collection.find_one({"id": 83})["img"],
                    self.beer_collection.find_one({"id": 83})["prices"])
        elif np.argmax(result) == 84:
            return (self.beer_collection.find_one({"id": 84})["name"], self.beer_collection.find_one({"id": 84})["img"],
                    self.beer_collection.find_one({"id": 84})["prices"])
        elif np.argmax(result) == 85:
            return (self.beer_collection.find_one({"id": 85})["name"], self.beer_collection.find_one({"id": 85})["img"],
                    self.beer_collection.find_one({"id": 85})["prices"])
        elif np.argmax(result) == 86:
            return (self.beer_collection.find_one({"id": 86})["name"], self.beer_collection.find_one({"id": 86})["img"],
                    self.beer_collection.find_one({"id": 86})["prices"])
        elif np.argmax(result) == 87:
            return (self.beer_collection.find_one({"id": 87})["name"], self.beer_collection.find_one({"id": 87})["img"],
                    self.beer_collection.find_one({"id": 87})["prices"])
        elif np.argmax(result) == 88:
            return (self.beer_collection.find_one({"id": 88})["name"], self.beer_collection.find_one({"id": 88})["img"],
                    self.beer_collection.find_one({"id": 88})["prices"])
        elif np.argmax(result) == 89:
            return (self.beer_collection.find_one({"id": 89})["name"], self.beer_collection.find_one({"id": 89})["img"],
                    self.beer_collection.find_one({"id": 89})["prices"])
        elif np.argmax(result) == 90:
            return (self.beer_collection.find_one({"id": 90})["name"], self.beer_collection.find_one({"id": 90})["img"],
                    self.beer_collection.find_one({"id": 90})["prices"])
        elif np.argmax(result) == 91:
            return (self.beer_collection.find_one({"id": 91})["name"], self.beer_collection.find_one({"id": 91})["img"],
                    self.beer_collection.find_one({"id": 91})["prices"])
        elif np.argmax(result) == 92:
            return (self.beer_collection.find_one({"id": 92})["name"], self.beer_collection.find_one({"id": 92})["img"],
                    self.beer_collection.find_one({"id": 92})["prices"])
        elif np.argmax(result) == 93:
            return (self.beer_collection.find_one({"id": 93})["name"], self.beer_collection.find_one({"id": 93})["img"],
                    self.beer_collection.find_one({"id": 93})["prices"])
        elif np.argmax(result) == 94:
            return (self.beer_collection.find_one({"id": 94})["name"], self.beer_collection.find_one({"id": 94})["img"],
                    self.beer_collection.find_one({"id": 94})["prices"])
        elif np.argmax(result) == 95:
            return (self.beer_collection.find_one({"id": 95})["name"], self.beer_collection.find_one({"id": 95})["img"],
                    self.beer_collection.find_one({"id": 95})["prices"])
        elif np.argmax(result) == 96:
            return (self.beer_collection.find_one({"id": 96})["name"], self.beer_collection.find_one({"id": 96})["img"],
                    self.beer_collection.find_one({"id": 96})["prices"])
        elif np.argmax(result) == 97:
            return (self.beer_collection.find_one({"id": 97})["name"], self.beer_collection.find_one({"id": 97})["img"],
                    self.beer_collection.find_one({"id": 97})["prices"])
        elif np.argmax(result) == 98:
            return (self.beer_collection.find_one({"id": 98})["name"], self.beer_collection.find_one({"id": 98})["img"],
                    self.beer_collection.find_one({"id": 98})["prices"])
        elif np.argmax(result) == 99:
            return (self.beer_collection.find_one({"id": 99})["name"], self.beer_collection.find_one({"id": 99})["img"],
                    self.beer_collection.find_one({"id": 99})["prices"])
        elif np.argmax(result) == 100:
            return (
            self.beer_collection.find_one({"id": 100})["name"], self.beer_collection.find_one({"id": 100})["img"],
            self.beer_collection.find_one({"id": 100})["prices"])
        elif np.argmax(result) == 101:
            return (
            self.beer_collection.find_one({"id": 101})["name"], self.beer_collection.find_one({"id": 101})["img"],
            self.beer_collection.find_one({"id": 101})["prices"])
        elif np.argmax(result) == 102:
            return (
            self.beer_collection.find_one({"id": 102})["name"], self.beer_collection.find_one({"id": 102})["img"],
            self.beer_collection.find_one({"id": 102})["prices"])
        elif np.argmax(result) == 103:
            return (
            self.beer_collection.find_one({"id": 103})["name"], self.beer_collection.find_one({"id": 103})["img"],
            self.beer_collection.find_one({"id": 103})["prices"])
        elif np.argmax(result) == 104:
            return (
            self.beer_collection.find_one({"id": 104})["name"], self.beer_collection.find_one({"id": 104})["img"],
            self.beer_collection.find_one({"id": 104})["prices"])
        elif np.argmax(result) == 105:
            return (
            self.beer_collection.find_one({"id": 105})["name"], self.beer_collection.find_one({"id": 105})["img"],
            self.beer_collection.find_one({"id": 105})["prices"])
        elif np.argmax(result) == 106:
            return (
            self.beer_collection.find_one({"id": 106})["name"], self.beer_collection.find_one({"id": 106})["img"],
            self.beer_collection.find_one({"id": 106})["prices"])
        elif np.argmax(result) == 107:
            return (
            self.beer_collection.find_one({"id": 107})["name"], self.beer_collection.find_one({"id": 107})["img"],
            self.beer_collection.find_one({"id": 107})["prices"])
        elif np.argmax(result) == 108:
            return (
            self.beer_collection.find_one({"id": 108})["name"], self.beer_collection.find_one({"id": 108})["img"],
            self.beer_collection.find_one({"id": 108})["prices"])
        elif np.argmax(result) == 109:
            return (
            self.beer_collection.find_one({"id": 109})["name"], self.beer_collection.find_one({"id": 109})["img"],
            self.beer_collection.find_one({"id": 109})["prices"])
        elif np.argmax(result) == 110:
            return (
            self.beer_collection.find_one({"id": 110})["name"], self.beer_collection.find_one({"id": 110})["img"],
            self.beer_collection.find_one({"id": 110})["prices"])
        elif np.argmax(result) == 111:
            return (
            self.beer_collection.find_one({"id": 111})["name"], self.beer_collection.find_one({"id": 111})["img"],
            self.beer_collection.find_one({"id": 111})["prices"])
        elif np.argmax(result) == 112:
            return (
            self.beer_collection.find_one({"id": 112})["name"], self.beer_collection.find_one({"id": 112})["img"],
            self.beer_collection.find_one({"id": 112})["prices"])
        elif np.argmax(result) == 113:
            return (
            self.beer_collection.find_one({"id": 113})["name"], self.beer_collection.find_one({"id": 113})["img"],
            self.beer_collection.find_one({"id": 113})["prices"])
        elif np.argmax(result) == 114:
            return (
            self.beer_collection.find_one({"id": 114})["name"], self.beer_collection.find_one({"id": 114})["img"],
            self.beer_collection.find_one({"id": 114})["prices"])
        elif np.argmax(result) == 115:
            return (
            self.beer_collection.find_one({"id": 115})["name"], self.beer_collection.find_one({"id": 115})["img"],
            self.beer_collection.find_one({"id": 115})["prices"])
        elif np.argmax(result) == 116:
            return (
            self.beer_collection.find_one({"id": 116})["name"], self.beer_collection.find_one({"id": 116})["img"],
            self.beer_collection.find_one({"id": 116})["prices"])
        elif np.argmax(result) == 117:
            return (
            self.beer_collection.find_one({"id": 117})["name"], self.beer_collection.find_one({"id": 117})["img"],
            self.beer_collection.find_one({"id": 117})["prices"])
        elif np.argmax(result) == 118:
            return (
            self.beer_collection.find_one({"id": 118})["name"], self.beer_collection.find_one({"id": 118})["img"],
            self.beer_collection.find_one({"id": 118})["prices"])
        elif np.argmax(result) == 119:
            return (
            self.beer_collection.find_one({"id": 119})["name"], self.beer_collection.find_one({"id": 119})["img"],
            self.beer_collection.find_one({"id": 119})["prices"])
        elif np.argmax(result) == 120:
            return (
            self.beer_collection.find_one({"id": 120})["name"], self.beer_collection.find_one({"id": 120})["img"],
            self.beer_collection.find_one({"id": 120})["prices"])
        elif np.argmax(result) == 121:
            return (
            self.beer_collection.find_one({"id": 121})["name"], self.beer_collection.find_one({"id": 121})["img"],
            self.beer_collection.find_one({"id": 121})["prices"])
        elif np.argmax(result) == 122:
            return (
            self.beer_collection.find_one({"id": 122})["name"], self.beer_collection.find_one({"id": 122})["img"],
            self.beer_collection.find_one({"id": 122})["prices"])
        elif np.argmax(result) == 123:
            return (
            self.beer_collection.find_one({"id": 123})["name"], self.beer_collection.find_one({"id": 123})["img"],
            self.beer_collection.find_one({"id": 123})["prices"])
        elif np.argmax(result) == 124:
            return (
            self.beer_collection.find_one({"id": 124})["name"], self.beer_collection.find_one({"id": 124})["img"],
            self.beer_collection.find_one({"id": 124})["prices"])
        elif np.argmax(result) == 125:
            return (
            self.beer_collection.find_one({"id": 125})["name"], self.beer_collection.find_one({"id": 125})["img"],
            self.beer_collection.find_one({"id": 125})["prices"])
        elif np.argmax(result) == 126:
            return (
            self.beer_collection.find_one({"id": 126})["name"], self.beer_collection.find_one({"id": 126})["img"],
            self.beer_collection.find_one({"id": 126})["prices"])
        elif np.argmax(result) == 127:
            return (
            self.beer_collection.find_one({"id": 127})["name"], self.beer_collection.find_one({"id": 127})["img"],
            self.beer_collection.find_one({"id": 127})["prices"])
        elif np.argmax(result) == 128:
            return (
            self.beer_collection.find_one({"id": 128})["name"], self.beer_collection.find_one({"id": 128})["img"],
            self.beer_collection.find_one({"id": 128})["prices"])
        elif np.argmax(result) == 129:
            return (
            self.beer_collection.find_one({"id": 129})["name"], self.beer_collection.find_one({"id": 129})["img"],
            self.beer_collection.find_one({"id": 129})["prices"])
        elif np.argmax(result) == 130:
            return (
            self.beer_collection.find_one({"id": 130})["name"], self.beer_collection.find_one({"id": 130})["img"],
            self.beer_collection.find_one({"id": 130})["prices"])
        elif np.argmax(result) == 131:
            return (
            self.beer_collection.find_one({"id": 131})["name"], self.beer_collection.find_one({"id": 131})["img"],
            self.beer_collection.find_one({"id": 131})["prices"])
        elif np.argmax(result) == 132:
            return (
            self.beer_collection.find_one({"id": 132})["name"], self.beer_collection.find_one({"id": 132})["img"],
            self.beer_collection.find_one({"id": 132})["prices"])
        elif np.argmax(result) == 133:
            return (
            self.beer_collection.find_one({"id": 133})["name"], self.beer_collection.find_one({"id": 133})["img"],
            self.beer_collection.find_one({"id": 133})["prices"])
        elif np.argmax(result) == 134:
            return (
            self.beer_collection.find_one({"id": 134})["name"], self.beer_collection.find_one({"id": 134})["img"],
            self.beer_collection.find_one({"id": 134})["prices"])
        elif np.argmax(result) == 135:
            return (
            self.beer_collection.find_one({"id": 135})["name"], self.beer_collection.find_one({"id": 135})["img"],
            self.beer_collection.find_one({"id": 135})["prices"])
        elif np.argmax(result) == 136:
            return (
            self.beer_collection.find_one({"id": 136})["name"], self.beer_collection.find_one({"id": 136})["img"],
            self.beer_collection.find_one({"id": 136})["prices"])
        elif np.argmax(result) == 137:
            return (
            self.beer_collection.find_one({"id": 137})["name"], self.beer_collection.find_one({"id": 137})["img"],
            self.beer_collection.find_one({"id": 137})["prices"])
        elif np.argmax(result) == 138:
            return (
            self.beer_collection.find_one({"id": 138})["name"], self.beer_collection.find_one({"id": 138})["img"],
            self.beer_collection.find_one({"id": 138})["prices"])
        elif np.argmax(result) == 139:
            return (
            self.beer_collection.find_one({"id": 139})["name"], self.beer_collection.find_one({"id": 139})["img"],
            self.beer_collection.find_one({"id": 139})["prices"])
        elif np.argmax(result) == 140:
            return (
            self.beer_collection.find_one({"id": 140})["name"], self.beer_collection.find_one({"id": 140})["img"],
            self.beer_collection.find_one({"id": 140})["prices"])
        elif np.argmax(result) == 141:
            return (
            self.beer_collection.find_one({"id": 141})["name"], self.beer_collection.find_one({"id": 141})["img"],
            self.beer_collection.find_one({"id": 141})["prices"])
        elif np.argmax(result) == 142:
            return (
            self.beer_collection.find_one({"id": 142})["name"], self.beer_collection.find_one({"id": 142})["img"],
            self.beer_collection.find_one({"id": 142})["prices"])
        elif np.argmax(result) == 143:
            return (
            self.beer_collection.find_one({"id": 143})["name"], self.beer_collection.find_one({"id": 143})["img"],
            self.beer_collection.find_one({"id": 143})["prices"])
        elif np.argmax(result) == 144:
            return (
            self.beer_collection.find_one({"id": 144})["name"], self.beer_collection.find_one({"id": 144})["img"],
            self.beer_collection.find_one({"id": 144})["prices"])
        elif np.argmax(result) == 145:
            return (
            self.beer_collection.find_one({"id": 145})["name"], self.beer_collection.find_one({"id": 145})["img"],
            self.beer_collection.find_one({"id": 145})["prices"])
        elif np.argmax(result) == 146:
            return (
            self.beer_collection.find_one({"id": 146})["name"], self.beer_collection.find_one({"id": 146})["img"],
            self.beer_collection.find_one({"id": 146})["prices"])
        elif np.argmax(result) == 147:
            return (
            self.beer_collection.find_one({"id": 147})["name"], self.beer_collection.find_one({"id": 147})["img"],
            self.beer_collection.find_one({"id": 147})["prices"])
        elif np.argmax(result) == 148:
            return (
            self.beer_collection.find_one({"id": 148})["name"], self.beer_collection.find_one({"id": 148})["img"],
            self.beer_collection.find_one({"id": 148})["prices"])
        elif np.argmax(result) == 149:
            return (
            self.beer_collection.find_one({"id": 149})["name"], self.beer_collection.find_one({"id": 149})["img"],
            self.beer_collection.find_one({"id": 149})["prices"])
        elif np.argmax(result) == 150:
            return (
            self.beer_collection.find_one({"id": 150})["name"], self.beer_collection.find_one({"id": 150})["img"],
            self.beer_collection.find_one({"id": 150})["prices"])
        elif np.argmax(result) == 151:
            return (
            self.beer_collection.find_one({"id": 151})["name"], self.beer_collection.find_one({"id": 151})["img"],
            self.beer_collection.find_one({"id": 151})["prices"])
        elif np.argmax(result) == 152:
            return (
            self.beer_collection.find_one({"id": 152})["name"], self.beer_collection.find_one({"id": 152})["img"],
            self.beer_collection.find_one({"id": 152})["prices"])
        elif np.argmax(result) == 153:
            return (
            self.beer_collection.find_one({"id": 153})["name"], self.beer_collection.find_one({"id": 153})["img"],
            self.beer_collection.find_one({"id": 153})["prices"])
        elif np.argmax(result) == 154:
            return (
            self.beer_collection.find_one({"id": 154})["name"], self.beer_collection.find_one({"id": 154})["img"],
            self.beer_collection.find_one({"id": 154})["prices"])
        elif np.argmax(result) == 155:
            return (
            self.beer_collection.find_one({"id": 155})["name"], self.beer_collection.find_one({"id": 155})["img"],
            self.beer_collection.find_one({"id": 155})["prices"])
        elif np.argmax(result) == 156:
            return (
            self.beer_collection.find_one({"id": 156})["name"], self.beer_collection.find_one({"id": 156})["img"],
            self.beer_collection.find_one({"id": 156})["prices"])
        elif np.argmax(result) == 157:
            return (
            self.beer_collection.find_one({"id": 157})["name"], self.beer_collection.find_one({"id": 157})["img"],
            self.beer_collection.find_one({"id": 157})["prices"])
        elif np.argmax(result) == 158:
            return (
            self.beer_collection.find_one({"id": 158})["name"], self.beer_collection.find_one({"id": 158})["img"],
            self.beer_collection.find_one({"id": 158})["prices"])
        elif np.argmax(result) == 159:
            return (
            self.beer_collection.find_one({"id": 159})["name"], self.beer_collection.find_one({"id": 159})["img"],
            self.beer_collection.find_one({"id": 159})["prices"])
        elif np.argmax(result) == 160:
            return (
            self.beer_collection.find_one({"id": 160})["name"], self.beer_collection.find_one({"id": 160})["img"],
            self.beer_collection.find_one({"id": 160})["prices"])
        elif np.argmax(result) == 161:
            return (
            self.beer_collection.find_one({"id": 161})["name"], self.beer_collection.find_one({"id": 161})["img"],
            self.beer_collection.find_one({"id": 161})["prices"])
        elif np.argmax(result) == 162:
            return (
            self.beer_collection.find_one({"id": 162})["name"], self.beer_collection.find_one({"id": 162})["img"],
            self.beer_collection.find_one({"id": 162})["prices"])
        elif np.argmax(result) == 163:
            return (
            self.beer_collection.find_one({"id": 163})["name"], self.beer_collection.find_one({"id": 163})["img"],
            self.beer_collection.find_one({"id": 163})["prices"])
        elif np.argmax(result) == 164:
            return (
            self.beer_collection.find_one({"id": 164})["name"], self.beer_collection.find_one({"id": 164})["img"],
            self.beer_collection.find_one({"id": 164})["prices"])
        elif np.argmax(result) == 165:
            return (
            self.beer_collection.find_one({"id": 165})["name"], self.beer_collection.find_one({"id": 165})["img"],
            self.beer_collection.find_one({"id": 165})["prices"])
        elif np.argmax(result) == 166:
            return (
            self.beer_collection.find_one({"id": 166})["name"], self.beer_collection.find_one({"id": 166})["img"],
            self.beer_collection.find_one({"id": 166})["prices"])
        elif np.argmax(result) == 167:
            return (
            self.beer_collection.find_one({"id": 167})["name"], self.beer_collection.find_one({"id": 167})["img"],
            self.beer_collection.find_one({"id": 167})["prices"])
        elif np.argmax(result) == 168:
            return (
            self.beer_collection.find_one({"id": 168})["name"], self.beer_collection.find_one({"id": 168})["img"],
            self.beer_collection.find_one({"id": 168})["prices"])
        elif np.argmax(result) == 169:
            return (
            self.beer_collection.find_one({"id": 169})["name"], self.beer_collection.find_one({"id": 169})["img"],
            self.beer_collection.find_one({"id": 169})["prices"])
        elif np.argmax(result) == 170:
            return (
            self.beer_collection.find_one({"id": 170})["name"], self.beer_collection.find_one({"id": 170})["img"],
            self.beer_collection.find_one({"id": 170})["prices"])
        elif np.argmax(result) == 171:
            return (
            self.beer_collection.find_one({"id": 171})["name"], self.beer_collection.find_one({"id": 171})["img"],
            self.beer_collection.find_one({"id": 171})["prices"])
        elif np.argmax(result) == 172:
            return (
            self.beer_collection.find_one({"id": 172})["name"], self.beer_collection.find_one({"id": 172})["img"],
            self.beer_collection.find_one({"id": 172})["prices"])
        elif np.argmax(result) == 173:
            return (
            self.beer_collection.find_one({"id": 173})["name"], self.beer_collection.find_one({"id": 173})["img"],
            self.beer_collection.find_one({"id": 173})["prices"])
        elif np.argmax(result) == 174:
            return (
            self.beer_collection.find_one({"id": 174})["name"], self.beer_collection.find_one({"id": 174})["img"],
            self.beer_collection.find_one({"id": 174})["prices"])
        else:
            return "Вибач, але я не знайшов твоє пиво..."
