import pymongo
import os
from beer_full_names import BeerNames
import inspect

#установим соединение с Mongo DB
db_client = pymongo.MongoClient("mongodb://localhost:27017/")

#подключаемся к БД
current_db = db_client["products_db"]

#создаем коллекцию beers
beer_collection = current_db["beers"]


# amstel_svitle_05l_glass = {
#     "name":BEER_5_0_ORIGINAL_LAGER_SVITLE_0_5_JB,
#     "text":"beer_5_0_Original_Lager_svitle_05_l_jb.txt",
#     "img":"../beerBot_DATA/pics/beer_5_0_original_lager__svitle_0_5_l_jb.png"
# }

path = "../beerBot_DATA/all_beers"
all_pics_path = "../beerBot_DATA/pics/all_beers"
pics_dir = os.listdir(all_pics_path)

#формируем список названий пива
all_names = inspect.getmembers(BeerNames)
all_names = all_names[:170]
all_beers_names = [x[1] for x in all_names]

#создадим словарь с продуктами для добавления в БД
additional_data = []

for i, file in enumerate(os.listdir(path)):
    #print(f"File:#{i} {file}")
    add_item = {"name":all_beers_names[i], "text":file, "img": pics_dir[i]}
    additional_data.append(add_item)

# print(len(additional_data))
# print(additional_data)

# beer_collection.delete_many({})
# beer_collection.insert_many(additional_data)
