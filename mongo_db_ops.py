import pymongo
#from beer_full_names import *
#from beer_bot_utils import get_texts_refers_from_DB
from adding_data import additional_data

#установим соединение с Mongo DB
db_client = pymongo.MongoClient("mongodb://localhost:27017/")

#подключаемся к БД, если ее нет, то она будет создана
current_db = db_client["products_db"]

#создаем коллекцию beers
beer_collection = current_db["beers"]


# #создадим одно пиво
# amstel_svitle_05l_glass = {
#     "name":BEER_5_0_ORIGINAL_LAGER_SVITLE_0_5_JB,
#     "text":"beer_5_0_Original_Lager_svitle_05_l_jb.txt",
#     "img":"../beerBot_DATA/pics/beer_5_0_original_lager__svitle_0_5_l_jb.png"
# }
#
# #добавим этот документ в коллекцию beers
# ins_result = beer_collection.insert_one(amstel_svitle_05l_glass)
# print(ins_result.inserted_id)   #id втсавленного документа
#
# #вставим остальные документы
# texts_refs = get_texts_refers_from_DB()
# all_beers = []
# for i in range(9):
#     all_beers.append({"name":NAMES[i], "text":texts_refs[i + 1], "img":""})
#
# all_beers[0]["img"] = "../beerBot_DATA/pics/5_0_original_pils_svitle_0_5_jb.png"
# all_beers[1]["img"] = "../beerBot_DATA/pics/5_0_original_weiss_beer_0_5_jb.png"
# all_beers[2]["img"] = "../beerBot_DATA/pics/5_0_original_craft_0_5_jb.png"
# all_beers[3]["img"] = "../beerBot_DATA/pics/amstel_svitle_0_5_glass.png"
# all_beers[4]["img"] = "../beerBot_DATA/pics/amstel_svitle_0_5_jb.png"
# all_beers[5]["img"] = "../beerBot_DATA/pics/arsenal_micne_05_glass.png"
# all_beers[6]["img"] = "../beerBot_DATA/pics/arsenal_micne_2L_pl.png"
# all_beers[7]["img"] = "../beerBot_DATA/pics/bavaria_granat_bezalk_svetl_05jb.png"
# all_beers[8]["img"] = "../beerBot_DATA/pics/bavaria_liquid_apple_svitle_bezalk_05_jb.png"
#
#
# ins_res = beer_collection.insert_many(all_beers)
#
#
#
beer_collection.delete_many({})
#beer_collection.insert_many(additional_data)
