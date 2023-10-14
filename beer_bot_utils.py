import pymongo

def make_list(count: int, pos: int) -> list:
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    # проверяем аргументы на принадлежность к типу int:
    if type(count) != int or type(pos) != int:
        raise TypeError("Arguments count and pos for function 'make_list' must be int!")
    # создаем вложенный список:
    res = [[0 for x in range(count)]]
    res[0][pos] = 1
    return res


class BeersDB:
    # установим соединение с Mongo DB
    __db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # подключаемся к БД
    __current_db = __db_client["products_db"]
    beers_collection = __current_db["beers"]


class RefersForRNN(BeersDB):
    '''Класс для подготовки текстовых файлов перед обучением НС.'''

    def add_new_item(self, path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f"../beerBot_DATA/texts/{path_tail}"

        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def get_text_from_DB(self):
        '''Загрзука обучающего текста и его обработка перед обучением НС'''

        texts = []
        count_item_list = []

        for item in self.beers_collection.find():
            item_text = self.add_new_item(item["text"])
            count_item = len(item_text)
            count_item_list.append(count_item)
            texts += item_text

        return texts, count_item_list


class GetBeerData(BeersDB):

    def __init__(self, rnn_respond:str):
        self.__rnn_respond = rnn_respond

    def send_data(self) -> str:

        # производим проверку и возвращаем нужную картинку

        if self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво 5.0 Original Lager светлое 0.5 в ж.б"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво 5.0 Original Lager светлое 0.5 в ж.б"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво 5.0 Original pills светлое 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво 5.0 Original pills светлое 0,5 л в банке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one(
                {"name": "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво 5.0 original weiss нефильтрованное светлое 0,5 л в банке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво 5.0 origin craft beer нефильтрованное светлое 0,5 л в банке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво amstel светлое 0,5 л в бутылке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво amstel светлое 0,5 л в бутылке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво amstel светлое 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво amstel светлое 0,5 л в банке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво арсенал крепкое 0,5 л в бутылке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво арсенал крепкое 0,5 л в бутылке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво арсенал крепкое светлое 2 л в бутылке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво арсенал крепкое светлое 2 л в бутылке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво bavaria гранат безалкогольное светлое 0,5 л в банке"})["img"]

        elif self.__rnn_respond == self.beers_collection.find_one({"name": "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"})["name"]:
            return self.beers_collection.find_one({"name": "Пиво bavaria liquid apple светлое безалкогольное 0,5 л в банке"})["img"]

        else:
            return ""
