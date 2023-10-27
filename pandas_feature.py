import pandas as pd
from pandas import DataFrame
from pandas.plotting import table
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator, FixedLocator, FormatStrFormatter
import numpy as np
import pymongo

def make_price_pic():
    '''Generates image with item's all prices
    and plot with compared prices.'''

    # установим соединение с Mongo DB
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")

    # подключаемся к БД
    current_db = db_client["products_db"]

    # создаем коллекцию beers
    beer_collection = current_db["beers"]

    first_beer = beer_collection.find_one({"id":13})

    markets = ["АТБ", "ЕКО", "Varus", "Сільпо", "Ашан", "Novus", "Metro", "НК", "Fozzy"]
    prices = [x for x in first_beer['prices'].values()]

    market_colors = ['blue', 'orange', 'green',
                     'red', 'purple', 'brown',
                     'pink', 'grey', 'olive']
    print(prices)


    data = {"Цена":prices}
    df = DataFrame(data, index=markets)

    # ax = plt.subplot(111, frame_on=False)
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    # table(ax, df, loc="center")
    # plt.savefig("my_table.png")


    #create plot
    fig = plt.figure(figsize=(7,4))
    ax = fig.add_subplot()

    colors_diff = []
    for value in prices:
        if value == min(prices):
            colors_diff.append("red")
        else:
            colors_diff.append("blue")

    ax.bar(markets, (prices), color = colors_diff)



    #ax.set(ylim = (0, max(prices)))
    #ax.set_ylim(ymin = 0, ymax = max(prices))
    ax.yaxis.set_major_locator(MaxNLocator(10))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    #ax.yaxis.set_major_locator(FixedLocator([0, 10, 20, 30, 50, 75, 100]))

    #ax.grid()
    plt.title("Ціни у маркетах, грн")
    plt.show()
    #plt.savefig('compared_prices.png')





make_price_pic()