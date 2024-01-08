from project.food.main_dish import MainDish


class Salmon(MainDish):
    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)
    GRAMS = 22
