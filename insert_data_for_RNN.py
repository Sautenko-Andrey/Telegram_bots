import pymongo


class InsertData:
    '''Opens DB and inserts a new item inside.'''

    # установим соединение с Mongo DB
    __db_client = pymongo.MongoClient("mongodb://localhost:27017/")

    # подключаемся к БД
    __current_db = __db_client["products_db"]

    # создаем коллекцию beers
    __beer_collection = __current_db["beers"]

    @classmethod
    def __check_args(cls, id, text, img, name) -> None:
        '''Checks arguments of instance of the class InsertData'''

        if type(id) != int:
            raise TypeError("Type of id argument must be int and greater to 0.")
        if id < 0:
            raise AttributeError("id value must be greater to 0.")
        if type(text) != str or type(img) != str or type(name)!= str:
            raise TypeError("Type of text, img and name arguments must be string.")


    def __init__(self, id:int, text:str, img:str, name:str):

        # Checking args
        self.__check_args(id, text, img, name)

        # Creating a new item
        self.__new_item = {
            "id":id,
            "text":text,
            "img":img,
            "name":name
        }


    def __call__(self, *args, **kwargs):

        # Inserting a new item into DB
        self.__beer_collection.insert_one(self.__new_item)

head_path = "../beerBot_DATA/pics/all_beers/"

adding = InsertData(id = 234,
                    text = 'beer_john_gaspar_temne_033_l_glass.txt',
                    img = f"{head_path}235_beer_john_gaspar_temne_033_glass.png",
                    name = "Пиво John Gaspar темне, 0,33л")
adding()
