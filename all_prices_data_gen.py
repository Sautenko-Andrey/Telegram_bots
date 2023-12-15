from bot_parcer import Parsers_list
import pymongo

class PricesGeneration:
    '''Class updates/sets prices for all items in DB,
    or does the same with the only desired item in the DB.'''

    # properties of MongoDB
    __HOST = "mongodb://localhost:27017/"
    __DB_NAME = "products_db"
    __CURRENT_DB = "beers"

    # properties of data
    __ITEMS_AMOUNT = 235

    __slots__ = ("__db_client", "__current_db", "__beer_collection")

    @classmethod
    def __check_id(cls, id) -> None:
        '''Checks id'''

        if not isinstance(id, int):
            raise TypeError(f"Error: incorrect argument id: {id}")
        if id < 0:
            raise AttributeError(f"Error: {id} < 0")

    def __init__(self):
        self.__db_client = pymongo.MongoClient(self.__HOST)
        self.__current_db = self.__db_client[self.__DB_NAME]
        self.__beer_collection = self.__current_db[self.__CURRENT_DB]

    def __query(self, item_id: int) -> None:
        '''MongoDB query for data generation'''

        self.__check_id(item_id)

        self.__beer_collection.update_one({"id": item_id}, {"$set": {
            "prices": {
                "atb": Parsers_list[item_id]()[0],
                "eko": Parsers_list[item_id]()[1],
                "varus": Parsers_list[item_id]()[2],
                "silpo": Parsers_list[item_id]()[3],
                "ashan": Parsers_list[item_id]()[4],
                "novus": Parsers_list[item_id]()[5],
                "metro": Parsers_list[item_id]()[6],
                "nk": Parsers_list[item_id]()[7],
                "fozzy": Parsers_list[item_id]()[8]
            }
        }})

    def price_update_all(self) -> None:
        '''Generated price data for the all items in the DB'''

        for i in range(self.__ITEMS_AMOUNT):
            self.__query(i)

    def price_update_one(self, item_id: int) -> None:
        '''Updates/sets prices in the particular item in the DB'''

        # update prices
        self.__query(item_id)

    def price_update_group(self, *args) -> None:
        '''Updates/sets prices in the group of items in the DB'''

        # Check args
        for i in args:
            self.__check_id(i)

        # Compute numbers of the upcoming iterations in the loop
        num_iterations = len(args)

        # Update prices in the particular items
        for i in range(num_iterations):
            self.__query(args[i])

    def price_update_range(self, start:int, finish:int) -> None:
        '''Updates/sets prices in the chosen range of indexes.'''

        # Check arguments
        self.__check_id(start)
        self.__check_id(finish)

        # Update prices in the particular range of indexes.
        for i in range(start, finish + 1):
            self.__query(i)





data_gen_ex = PricesGeneration()
#data_gen_ex.price_update_one(191)
#data_gen_ex.price_update_group(194, 195, 196, 197, 198, 199, 200)
data_gen_ex.price_update_range(227,235)

# Old version

# def price_update():
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
#     items_amount = 218
#
#     for i in range(items_amount):
#
#         beer_collection.update_one({"id": i}, {"$set": {
#             "prices": {
#                 "atb": Parsers_list[i]()[0],
#                 "eko": Parsers_list[i]()[1],
#                 "varus": Parsers_list[i]()[2],
#                 "silpo": Parsers_list[i]()[3],
#                 "ashan": Parsers_list[i]()[4],
#                 "novus": Parsers_list[i]()[5],
#                 "metro": Parsers_list[i]()[6],
#                 "nk": Parsers_list[i]()[7],
#                 "fozzy": Parsers_list[i]()[8]
#             }
#         }})

# price_update()


# def price_update_one(item_id: int) -> None:
#
#     '''Updates/sets prices in the particular item'''
#
#     if not isinstance(item_id, int):
#         raise TypeError(f"Error: incorrect argument id: {item_id}")
#     if item_id < 0:
#         raise AttributeError(f"Error: {item_id} < 0")
#
#     # connection to Mongo DB
#     db_client = pymongo.MongoClient("mongodb://localhost:27017/")
#
#     # connection to products_db DB
#     current_db = db_client["products_db"]
#
#     # create collection
#     beer_collection = current_db["beers"]
#
#     # update prices
#     beer_collection.update_one({"id": item_id}, {"$set": {
#             "prices": {
#                 "atb": Parsers_list[item_id]()[0],
#                 "eko": Parsers_list[item_id]()[1],
#                 "varus": Parsers_list[item_id]()[2],
#                 "silpo": Parsers_list[item_id]()[3],
#                 "ashan": Parsers_list[item_id]()[4],
#                 "novus": Parsers_list[item_id]()[5],
#                 "metro": Parsers_list[item_id]()[6],
#                 "nk": Parsers_list[item_id]()[7],
#                 "fozzy": Parsers_list[item_id]()[8]
#             }
#         }})

# price_update_one(190)
