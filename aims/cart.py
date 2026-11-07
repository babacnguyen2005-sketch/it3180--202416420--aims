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

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("**************************************************")
