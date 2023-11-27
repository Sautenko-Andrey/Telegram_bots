import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import keras
from tensorflow import keras
from keras.layers import Dense, Embedding, LSTM
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

from beer_bot_utils import *



class RNN_beerBot:

    #addding slots for memory safe and get more speed
    __slots__ = ("model")

    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 3000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    # количество продуктов
    ITEMS_AMOUNT = 179


    def __init__(self):
        '''Инициализация модели НС и ее подготовка к обучению'''

        self.model = keras.Sequential([
            Embedding(self.MAX_WORDS, self.ITEMS_AMOUNT, input_length=self.MAX_LENGTH_TEXT),
            LSTM(self.ITEMS_AMOUNT, return_sequences=True),
            LSTM(self.ITEMS_AMOUNT),
            Dense(self.ITEMS_AMOUNT, activation='softmax')
        ])

        self.model.compile(optimizer=Adam(0.0001), loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def training_NN(self):
        '''Метод обучения НС'''

        # загружаем подготовленные данные для обучения:
        TRAIN_DATA, TARGET_DATA, tokenizer = self.converted_data()

        # запускаем тренировку:
        history = self.model.fit(TRAIN_DATA, TARGET_DATA, epochs=15, batch_size=32)   #15 epochs enough

        reverse_word_map = dict(map(reversed, self.converted_data()[2].word_index.items()))

        # сохраняем модель обученной НС:
        self.model.save('beer_bot_model_text')
        print('Обучение нейронной сети успешно завершено.')

        # printing grafics
        self.get_grafic(history.history)

        return history, reverse_word_map

    def upload_data(self):
        """Функция загрузки обучающей выборки для каждой позиции товара"""

        # создаем єкземпляр класса RefersForRNN:
        all_text_data = RefersForRNN()
        return all_text_data.get_text_from_DB()

    def converted_data(self):
        '''Подготовка обучающих данных'''

        # загружаем общую папку с текстами для обработки:
        texts = self.upload_data()[0]

        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(texts)

        # формируем последовательность из чисел вместо слов
        # (будут индексы каждых слов вместо слов)
        data = tokenizer.texts_to_sequences(texts)

        # короткие тексты дополняем нулями, а длинные урезаем до 10 слов:
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # окончательно формируем обучающую выборку:
        TRAIN_SAMPLE = data_pad
        items = self.ITEMS_AMOUNT

        result = []
        for i in range(items):
            data_list = [make_list(items, i) * self.upload_data()[1][i] for x in range(1)]
            for j in data_list:
                for k in j:
                    result.append(k)

        TARGET_SAMPLE = np.mat(result)

        # перемешиваем обучающую выборку для лучшей тренированности НС:
        # создаем рандомные индексы:
        indeces = np.random.choice(TRAIN_SAMPLE.shape[0], size=TRAIN_SAMPLE.shape[0],
                                   replace=False)

        # перемешиаем обучающую и целевую выборки:
        TRAIN_SAMPLE = TRAIN_SAMPLE[indeces]
        TARGET_SAMPLE = TARGET_SAMPLE[indeces]

        return TRAIN_SAMPLE, TARGET_SAMPLE, tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = self.training_NN()[1]
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def defining_item(self, user_text):
        '''Метод определения товара по тексту, который запрашивает пользователь '''

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.converted_data()[2]
        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # смотрим какую на самом деле фразу мы анализируем(т.к. некоторых слов у нас может не быть в словаре)
        print(self.index_convert_to_text(data[0]))


        result = self.model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')

    def get_grafic(self, history_dict: dict):
        accuracy = history_dict["accuracy"]
        loss = history_dict["loss"]
        epochs = range(1, len(accuracy) + 1)

        fig = plt.figure(figsize=(8, 6))
        plt.plot(epochs, accuracy, color="red", marker="o", label="Accuracy")
        plt.plot(epochs, loss, color="blue", marker="o", label="Loss")
        plt.title("Accuracy and losses during training")
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy/Loss")
        plt.grid()
        plt.legend()
        plt.show()


user = RNN_beerBot()
user.training_NN()
