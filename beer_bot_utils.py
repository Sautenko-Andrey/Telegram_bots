def make_list(count: int, pos: int) -> list:
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    # проверяем аргументы на принадлежность к типу int:
    if type(count) != int or type(pos) != int:
        raise TypeError("Arguments count and pos for function 'make_list' must be int!")
    # создаем вложенный список:
    res = [[0 for x in range(count)]]
    res[0][pos] = 1
    return res


def get_texts_refers_from_DB():
    '''Сбор всех ссылок на текстовые файлы для обучения RNN'''
    #return AllTextsStorage.objects.all()
    all_refers = (
        "beer_5_0_Original_Lager_svitle_05_l_jb.txt",
        "beer_5_0_OriginalPills_svitle_05_l_jb.txt",
        "beer_5_0_Original_Weiss_sv_nef_05_l_jb.txt",
        "beer_5_0_origin_craft_nef_sv_05_l_jb.txt",
        "beer_amstel_svitle_05_l_glass.txt",
        "beer_amstel_svitle_05_l_jb.txt",
        "beer_arsenal_micne_05_l_glass.txt",
        "beer_arsenal_micne_svitle_2l_plastic.txt",
        "beer_bavaria_granat_bezalkogol_svitle_05_l_jb.txt",
        "beer_bavaria_liquid_app_0al_sv_05_l_jb.txt"
    )

    return all_refers


class RefersForRNN:
    '''Класс для подготовки текстовых файлов перед обучением НС.'''

    def add_new_item(self, path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        #path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'  #for local
        path = f"../beerBot_DATA/texts/{path_tail}"

        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def get_text_from_DB(self):
        '''Загрзука обучающего текста и его обработка перед обучением НС'''

        texts = []
        count_item_list = []
        for item in get_texts_refers_from_DB():
            #item_text = self.add_new_item(item.item_text_file)  #???
            item_text = self.add_new_item(item)
            count_item = len(item_text)
            count_item_list.append(count_item)
            texts += item_text

        return texts, count_item_list