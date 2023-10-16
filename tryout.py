import os
path = "../beerBot_DATA/all_beers"

# for file in os.listdir(path):
#     print(file)
#     with open(f"../beerBot_DATA/all_beers/{file}") as item_text:
#         print(item_text.readline())
#         break
text_dir = os.listdir(path)
with open(path +"/"+text_dir[0]) as file:
    print(file.readline())