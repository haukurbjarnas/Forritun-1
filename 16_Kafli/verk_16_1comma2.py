class WaterBottle:
    def __init__(self, maximum_capacity = 2):
        self.max_capacity = maximum_capacity
        self.current_contents = 0

    def fill(self):
        self.current_contents = self.max_capacity

    def drink(self, amount: int):
        if amount < 0:
            return 0
        elif amount > self.current_contents:
            drank_amount = self.current_contents
            self.current_contents = 0
            return drank_amount
        else:
            self.current_contents -= amount
            return amount
    
    def __str__(self):
        return f"The bottle currently holds {self.current_contents:.1f}L of water."