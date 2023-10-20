import os
import pymongo

#установим соединение с Mongo DB
db_client = pymongo.MongoClient("mongodb://localhost:27017/")

#подключаемся к БД
current_db = db_client["products_db"]

#создаем коллекцию beers
beer_collection = current_db["beers"]


adding_data_list = []

path = "../beerBot_DATA/all_beers"
files = [x for x in os.listdir(path)]

pics_path = '../beerBot_DATA/pics/all_beers'
pics = [x for x in os.listdir(pics_path)]
pics.sort()

id = 0
for i in files:
    add_item = {"id":id,"text":i, "img":f"../beerBot_DATA/pics/all_beers/{pics[id]}"}
    id+=1
    with open(path + '/' + i , "r") as f:
        first_line = f.readline()[0].upper() + f.readline()[1:]
        add_item.update({"name":first_line})
        adding_data_list.append(add_item)


beer_collection.delete_many({})
beer_collection.insert_many(adding_data_list)