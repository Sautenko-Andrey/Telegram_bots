import pymongo
from bson import ObjectId

#установим соединение с Mongo DB
db_client = pymongo.MongoClient("mongodb://localhost:27017/")

#подключаемся к БД
current_db = db_client["products_db"]

#создаем коллекцию beers
beer_collection = current_db["beers"]

# beer_names = []
# for item in beer_collection.find():
#     #print(item["name"])
#     beer_names.append(item["name"])

# first = beer_collection.find()[0]
#
# for i in beer_collection.find():
#     print(i["name"])





