MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def total_cost(self):
        return sum(item.cost for item in self.items)
