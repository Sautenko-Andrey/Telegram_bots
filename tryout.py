# import os
# path = "../beerBot_DATA/all_beers"
#
# # for file in os.listdir(path):
# #     print(file)
# #     with open(f"../beerBot_DATA/all_beers/{file}") as item_text:
# #         print(item_text.readline())
# #         break
# text_dir = os.listdir(path)
# with open(path +"/"+text_dir[0]) as file:
#     print(file.readline())

atb = 10
eko = 0
varus = 2
out_of_stock = 'нет в наличии'

msg = "Prices\nATB: " + (str(atb) if atb > 0 else out_of_stock) + "\nЕКО: " + (str(eko) if eko > 0 else out_of_stock)
print(msg)