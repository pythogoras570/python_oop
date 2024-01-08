from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def grams(self):
        return self.__milliliters
