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

    #получаем доступ к папке с текстовыми файлами
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
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 1:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 2:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 3:
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
        elif np.argmax(result) == 9:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        if np.argmax(result) == 10:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 11:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 12:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        if np.argmax(result) == 13:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 14:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 15:
            return "Пиво amstel светлое 0,5 л в банке"
        if np.argmax(result) == 16:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 17:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 18:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 19:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 20:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 21:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 22:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 23:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 24:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 25:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 26:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 27:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 28:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 29:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 30:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 31:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 32:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 33:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 34:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 35:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 36:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 37:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 38:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 39:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 40:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 41:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 42:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 43:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 44:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 45:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 46:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 47:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 48:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 49:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 50:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 51:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 52:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 53:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 54:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 55:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 56:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 57:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 58:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 59:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 60:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 61:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 62:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 63:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 64:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 65:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 66:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 67:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 68:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 69:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 70:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 71:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 72:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 73:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 74:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 75:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 76:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 77:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 78:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 79:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 80:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 81:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 82:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 83:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 84:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 85:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 86:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 87:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 88:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 89:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 90:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 91:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 92:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 93:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 94:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 95:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 96:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 97:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 98:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 99:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 100:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 101:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 102:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 103:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 104:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 105:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 106:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 107:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 108:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 109:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 110:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 111:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 112:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 113:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 114:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 115:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) ==116:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 117:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 118:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 119:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 120:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 121:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 122:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 123:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 124:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 125:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 126:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 127:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 128:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 129:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 130:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 131:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 132:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 133:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 134:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 135:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 136:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 137:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 138:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 139:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 140:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 141:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 142:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 143:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 144:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 145:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 146:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 147:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 148:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 149:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 150:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 151:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 152:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 153:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 154:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 155:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 156:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 157:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 158:
            return "Пиво amstel светлое 0,5 л в банке"
        elif np.argmax(result) == 159:
            return "Пиво арсенал крепкое 0,5 л в бутылке"
        elif np.argmax(result) == 160:
            return "Пиво арсенал крепкое светлое 2 л в бутылке"
        elif np.argmax(result) == 161:
            return "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"
        elif np.argmax(result) == 162:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 163:
            return "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"
        elif np.argmax(result) == 164:
            return "Пиво 5.0 Original Lager светлое 0.5 в ж.б"
        elif np.argmax(result) == 165:
            return "Пиво 5.0 Original pills светлое 0,5 л в банке"
        elif np.argmax(result) == 166:
            return "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 167:
            return "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"
        elif np.argmax(result) == 168:
            return "Пиво amstel светлое 0,5 л в бутылке"
        elif np.argmax(result) == 169:
            return "Пиво amstel светлое 0,5 л в банке"
        else:
            return "Вибач, але я не знайшов твоє пиво..."
