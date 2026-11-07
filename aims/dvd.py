class DigitalVideoDisc:
    def __init__(self, title, category="", cost=0.0):
        self.title = title
        self.category = category
        self.cost = cost

    def __str__(self):
        return f"DVD - {self.title} - {self.category} - {self.cost} $"
