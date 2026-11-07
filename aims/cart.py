MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def total_cost_with_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("**************************************************")
