from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    def __init__(self, name, price, caffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    MILLILITERS = 50
    PRICE = 3.50

    @property
    def caffeine(self):
        return self.__caffeine
