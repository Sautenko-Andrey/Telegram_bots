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
        path = f"../beerBot_DATA/all_beers/{path_tail}"

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
            #print(f"Добавляемое пиво в БД: {item_text[0]}")
            count_item = len(item_text)
            count_item_list.append(count_item)
            texts += item_text

        return texts, count_item_list


# class GetBeerData(BeersDB):
#
#     # установим соединение с Mongo DB
#     db_client = pymongo.MongoClient("mongodb://localhost:27017/")
#
#     # подключаемся к БД
#     current_db = db_client["products_db"]
#
#     # создаем коллекцию beers
#     beer_collection = current_db["beers"]
#
#     def __init__(self, rnn_respond:str):
#         self.__rnn_respond = rnn_respond
#
#     def send_data(self) -> str:
#
#         beers = BeerNames()
#
#         # производим проверку и возвращаем нужную картинку
#
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 2})["name"]:
#             return self.beer_collection.find_one({"id": 2})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 3})["name"]:
#             return self.beer_collection.find_one({"id": 3})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 4})["name"]:
#             return self.beer_collection.find_one({"id": 4})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 5})["name"]:
#             return self.beer_collection.find_one({"id": 5})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 6})["name"]:
#             return self.beer_collection.find_one({"id": 6})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 7})["name"]:
#             return self.beer_collection.find_one({"id": 7})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 8})["name"]:
#             return self.beer_collection.find_one({"id": 8})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 9})["name"]:
#             return self.beer_collection.find_one({"id": 9})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 10})["name"]:
#             return self.beer_collection.find_one({"id": 10})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 11})["name"]:
#             return self.beer_collection.find_one({"id": 11})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 12})["name"]:
#             return self.beer_collection.find_one({"id": 12})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 13})["name"]:
#             return self.beer_collection.find_one({"id": 13})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 14})["name"]:
#             return self.beer_collection.find_one({"id": 14})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 15})["name"]:
#             return self.beer_collection.find_one({"id": 15})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 16})["name"]:
#             return self.beer_collection.find_one({"id": 16})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 17})["name"]:
#             return self.beer_collection.find_one({"id": 17})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 18})["name"]:
#             return self.beer_collection.find_one({"id": 18})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 19})["name"]:
#             return self.beer_collection.find_one({"id": 19})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 20})["name"]:
#             return self.beer_collection.find_one({"id": 20})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 21})["name"]:
#             return self.beer_collection.find_one({"id": 21})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 22})["name"]:
#             return self.beer_collection.find_one({"id": 22})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 23})["name"]:
#             return self.beer_collection.find_one({"id": 23})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 24})["name"]:
#             return self.beer_collection.find_one({"id": 24})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 25})["name"]:
#             return self.beer_collection.find_one({"id": 25})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 26})["name"]:
#             return self.beer_collection.find_one({"id": 26})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 27})["name"]:
#             return self.beer_collection.find_one({"id": 27})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 28})["name"]:
#             return self.beer_collection.find_one({"id": 28})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 29})["name"]:
#             return self.beer_collection.find_one({"id": 29})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 30})["name"]:
#             return self.beer_collection.find_one({"id": 30})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 31})["name"]:
#             return self.beer_collection.find_one({"id": 31})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 32})["name"]:
#             return self.beer_collection.find_one({"id": 32})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 33})["name"]:
#             return self.beer_collection.find_one({"id": 33})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 34})["name"]:
#             return self.beer_collection.find_one({"id": 34})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 35})["name"]:
#             return self.beer_collection.find_one({"id": 35})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 36})["name"]:
#             return self.beer_collection.find_one({"id": 36})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 37})["name"]:
#             return self.beer_collection.find_one({"id": 37})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 38})["name"]:
#             return self.beer_collection.find_one({"id": 38})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 39})["name"]:
#             return self.beer_collection.find_one({"id": 39})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 40})["name"]:
#             return self.beer_collection.find_one({"id": 40})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 41})["name"]:
#             return self.beer_collection.find_one({"id": 41})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 42})["name"]:
#             return self.beer_collection.find_one({"id": 42})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 43})["name"]:
#             return self.beer_collection.find_one({"id": 43})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 44})["name"]:
#             return self.beer_collection.find_one({"id": 44})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 45})["name"]:
#             return self.beer_collection.find_one({"id": 45})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 46})["name"]:
#             return self.beer_collection.find_one({"id": 46})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 47})["name"]:
#             return self.beer_collection.find_one({"id": 47})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 48})["name"]:
#             return self.beer_collection.find_one({"id": 48})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 49})["name"]:
#             return self.beer_collection.find_one({"id": 49})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 50})["name"]:
#             return self.beer_collection.find_one({"id": 50})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id":51})["name"]:
#             return self.beer_collection.find_one({"id": 51})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 52})["name"]:
#             return self.beer_collection.find_one({"id": 52})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 53})["name"]:
#             return self.beer_collection.find_one({"id": 53})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 54})["name"]:
#             return self.beer_collection.find_one({"id": 54})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 55})["name"]:
#             return self.beer_collection.find_one({"id": 55})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 56})["name"]:
#             return self.beer_collection.find_one({"id": 56})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 57})["name"]:
#             return self.beer_collection.find_one({"id": 57})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 58})["name"]:
#             return self.beer_collection.find_one({"id": 58})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 59})["name"]:
#             return self.beer_collection.find_one({"id": 59})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 60})["name"]:
#             return self.beer_collection.find_one({"id": 60})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 61})["name"]:
#             return self.beer_collection.find_one({"id": 61})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 62})["name"]:
#             return self.beer_collection.find_one({"id": 62})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 63})["name"]:
#             return self.beer_collection.find_one({"id": 63})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 64})["name"]:
#             return self.beer_collection.find_one({"id": 64})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 65})["name"]:
#             return self.beer_collection.find_one({"id": 65})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 66})["name"]:
#             return self.beer_collection.find_one({"id": 66})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 67})["name"]:
#             return self.beer_collection.find_one({"id": 67})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 68})["name"]:
#             return self.beer_collection.find_one({"id": 68})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 69})["name"]:
#             return self.beer_collection.find_one({"id": 69})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 70})["name"]:
#             return self.beer_collection.find_one({"id": 70})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 71})["name"]:
#             return self.beer_collection.find_one({"id": 71})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 72})["name"]:
#             return self.beer_collection.find_one({"id": 72})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 73})["name"]:
#             return self.beer_collection.find_one({"id": 73})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 74})["name"]:
#             return self.beer_collection.find_one({"id": 74})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 75})["name"]:
#             return self.beer_collection.find_one({"id": 75})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 76})["name"]:
#             return self.beer_collection.find_one({"id": 76})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 77})["name"]:
#             return self.beer_collection.find_one({"id": 77})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 78})["name"]:
#             return self.beer_collection.find_one({"id": 78})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 79})["name"]:
#             return self.beer_collection.find_one({"id": 79})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 80})["name"]:
#             return self.beer_collection.find_one({"id": 80})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 81})["name"]:
#             return self.beer_collection.find_one({"id": 81})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 82})["name"]:
#             return self.beer_collection.find_one({"id": 82})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 83})["name"]:
#             return self.beer_collection.find_one({"id": 83})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 84})["name"]:
#             return self.beer_collection.find_one({"id": 84})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 85})["name"]:
#             return self.beer_collection.find_one({"id": 85})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 86})["name"]:
#             return self.beer_collection.find_one({"id": 86})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 87})["name"]:
#             return self.beer_collection.find_one({"id": 87})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 88})["name"]:
#             return self.beer_collection.find_one({"id": 88})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 89})["name"]:
#             return self.beer_collection.find_one({"id": 89})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 90})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
#         if self.__rnn_respond == self.beer_collection.find_one({"id": 0})["name"]:
#             return self.beer_collection.find_one({"id": 0})["img"]
#         elif self.__rnn_respond == self.beer_collection.find_one({"id": 1})["name"]:
#             return self.beer_collection.find_one({"id": 1})["img"]
