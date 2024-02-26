class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.goals = 0

    def add_goals(self, goals):
        self.goals += goals

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, Goals: {self.goals}"