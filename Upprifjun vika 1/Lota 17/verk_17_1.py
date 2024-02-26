class WaterBottle:

    def __init__(self, max_capacity=2):

        self.max_capacity = max_capacity

        self.contents = 0

    def fill(self):

        self.needed = self.max_capacity - self.contents

    def drink(self, amount):

        self.amount = amount

        if self.amount > self.contents:
            self.contents = 0
        elif self.amount < self.contents:
            self.contents = self.contents
        else:
            self.contents -= self.amount

    def __str__(self) -> str:
        return f"{self.amount}"
    

a_bottle = WaterBottle(5)

print(f"The max capicity of the water bottle is {a_bottle}L.")