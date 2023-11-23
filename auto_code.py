from transliterate import translit

class AutoCode:

    # for the bot_parcer.py
    __PATH_to_bot_parcer = "./bot_parcer.py"

    # for the beerRNN.py
    __PATH_to_beeerRNN = "./beerRNN.py"
    __ROW_to_chandge_beerRNN = 28

    # for the beerRNN_executor.py
    __PATH_to_beerRNN_executor = "./beerRNN_executor.py"


    # # for the groceryappNNtext.py
    # __PATH_to_groceryappNNtext = "../GroceryAppVol3/FBApp/my_app/groceryappNNtext.py"
    # __INSERT_ROW_groceryappNNtext = 39
    #
    # # for the utils.py
    # __PATH_to_utils = "../GroceryAppVol3/FBApp/my_app/utils.py"
    #
    # # for the parsers.py
    # __PATH_to_parsers = "../GroceryAppVol3/FBApp/my_app/parsers.py"
    #
    # # for the product_prices_DATA_batches.py
    # __PATH_to_product_prices_DATA_batches = "../GroceryAppVol3/FBApp/my_app/product_prices_DATA_batches.py"
    #
    # #for the tags.py
    # __PATH_to_tags = "../GroceryAppVol3/FBApp/my_app/templatetags/my_app_tags.py"
    #
    # #for item_full_names.py
    # __PATH_to_item_names = "../GroceryAppVol3/FBApp/my_app/items_full_names.py"
    #
    # #for testerRNN
    # __PATH_to_tester_RNN = "../GroceryAppVol3/FBApp/my_app/tester_for_groceryappNN_TEXT.py"


    __slots__ = ("__item_full_name", "__img_path", "__index", "prepeared_text")

    def __init__(self, item_full_name: str, img_path:str, index: int):
        self.__item_full_name = item_full_name   # full name of item
        self.__img_path = img_path      # path to image
        self.__index = index   # index in RNN executor
        self.prepeared_text = self.code_litters()

    def __call__(self, item_amount: int, line_num_utils: int,
                 line_num_parsers: int, line_product_prices_data: int, *args, **kwargs):

        # changing value of items in line №29 beerRNN.py
        self.__open_read_write_save(
            self.__PATH_to_beeerRNN,
            self.__ROW_to_chandge_beerRNN,
            f"    ITEMS_AMOUNT = {item_amount}\n"
        )
        # end of operation

        # appending new lines in the beerRNN_executor.py
        self.__open_read_write_save(
            self.__PATH_to_beerRNN_executor,
            line_num_utils,
            f"        elif np.argmax(result) == {self.__index}:\n"
            f"                     return ("
            f"                     self.beer_collection.find_one(" + f"{'id': {self.__index}})['name'], self.beer_collection.find_one({'id': {self.__index}})['img'],"
        )
        # end of operation

        # appending new lines in the parsers.py
        self.__open_read_write_save(
            self.__PATH_to_parsers,
            line_num_parsers,
            f"    def {self.prepeared_text}_parser(self):\n"
            f"        ''' {self.__item_full_name} '''\n        return self.prices_parsing([])"
        )
        # end of operation

        # appending new lines in the product_prices_DATA_batches.py
        self.__open_read_write_save(
            self.__PATH_to_product_prices_DATA_batches,
            line_product_prices_data,
            "            {'" + f"{self.prepeared_text}':" + '{' + f'\n                "atb": parser.{self.prepeared_text}_parser()[0],\n'
                                                            f'                "eko": parser.{self.prepeared_text}_parser()[1],\n'
                                                            f'                "varus": parser.{self.prepeared_text}_parser()[2],\n'
                                                            f'                "silpo": parser.{self.prepeared_text}_parser()[3],\n'
                                                            f'                "ashan": parser.{self.prepeared_text}_parser()[4],\n'
                                                            f'                "novus": parser.{self.prepeared_text}_parser()[5],\n'
                                                            f'                "metro": parser.{self.prepeared_text}_parser()[6],\n'
                                                            f'                "nash_kray": parser.{self.prepeared_text}_parser()[7],\n'
                                                            f'                "fozzy": parser.{self.prepeared_text}_parser()[8]\n' + '}},'
        )
        # end of operation

        #appending code into tags.py, items_full_names.py and testerRNN
        self.__write_code()
        #end

    def __open_read_write_save(self, path: str, line: int, new_text: str):
        with open(path, "r") as file:
            data = file.readlines()

        data[line] = new_text

        with open(path, "w") as file:
            file.writelines(data)

    def code_litters(self) -> str:
        eng_text = translit(self.__item_full_name, language_code='ru', reversed=True)
        new = []
        for let in eng_text:
            if let == " " or let == "," or let == "%" or let == "/" or let == "-":
                new.append("_")
                continue
            elif let == "'" or let == "«" or let == "»" or let == "’":
                new.append("")
                continue
            elif let == "ї":
                new.append("j")
                continue
            new.append(let)
        new_text = "".join(new)

        return new_text

    def __write_code(self):

        # writting code for tags
        with open(self.__PATH_to_tags, "a") as file:
            file.write(
                f"""'''Тэг,возвращающий информацию о "{self.__item_full_name}"'''\nget_{self.prepeared_text} = tag.create_tag(ItemsPicsFromNet,{self.__pk})\n""")

        # writting code for item_names
        with open(self.__PATH_to_item_names, "a") as file:
            file.write(f'{self.prepeared_text.upper()} = "{self.__item_full_name}"\n')

        # writting code for tester_RNN
        with open(self.__PATH_to_tester_RNN, "a") as file:
            file.write(f"        elif np.argmax(result) == {self.__index}:\n"f"            return {self.prepeared_text.upper()}\n")





add_item = AutoCode(
    "Йогурт Галичина Карпатський без цукру 2,2% пет, 550г",
    803,   #+1
    799  #+1
)

add_item(
    800,  #+1
    1938,  #+2
    7512,  #+15
    5858  #+10
)

