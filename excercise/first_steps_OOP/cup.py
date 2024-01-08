class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        capacity = self.size - self.quantity
        if capacity - quantity >= 0:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity
