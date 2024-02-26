class Darts:
    def __init__(self) -> None:
        self.player_points = [301, 301]
        self.move_counter = 1

    def get_input(self):
        number = input(f"Input points for Player {self.move_counter%2 + 1}: ")
        while not number.isdigit():
            print("Invalid input!")
            number = input(f"Input points for Player {self.move_counter%2 + 1}: ")
        return int(number)
    
    def set_points(self, number):
        if not self.player_points[self.move_counter%2] -  number < 0:
            self.player_points[self.move_counter%2] -= number
        print(f"Player {self.move_counter%2 + 1} remaining points: {self.player_points[self.move_counter%2]}")
    
    def is_winner(self):
        if self.player_points[self.move_counter%2] == 0:
            print(f"Player {self.move_counter%2 + 1} won!")
            return True
        return False

darts_game = Darts()

while not darts_game.is_winner():
    darts_game.move_counter += 1
    points = darts_game.get_input()
    darts_game.set_points(points)