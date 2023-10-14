import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model

from beer_bot_utils import *


class ExecutorRNN:
    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

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
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 1:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 2:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        if np.argmax(result) == 3:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 4:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 5:
            return "Пиво amstel светлое 0,5 л в банке"
        if np.argmax(result) == 6:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 7:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 8:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 9:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        else:
            return "Вибач, але я не знайшов твоє пиво..."
