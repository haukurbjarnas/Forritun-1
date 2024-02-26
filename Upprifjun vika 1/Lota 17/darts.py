class Darts:

    def __init__(self):

        self.score_1 = 301
        self.score_2 = 301
        self.player = None

    def accepting_points(self, player):

        self.player

        validation_of_points = 0

        while validation_of_points == 0:
            try:
                player_points = int(input(f"Input points for {self.player}: "))
                validation_of_points += 1
                return player_points
            except ValueError:
                print("Invalid input!")

    def progress_of_game(self, player):

        #self.player = player

        player_points_gained = self.accepting_points(self.player)

        if player_points_gained > self.score_1:
            pass
        else:
            self.score_1 -= player_points_gained

        print(f"{self.player} remaining points: {self.score_1}")

        return self.score_1
    
    def referee(self, player):

        self.player = player

        turn = self.progress_of_game(self.player)

        return turn
    

player_1_playing = Darts()

player_2_playing = Darts()

conformation_of_win = 0

while conformation_of_win == 0:
    player_1 = player_1_playing.referee("Player 1")
    if player_1 == 0:
        print("Player 1 won!")
        exit()
    player_2 = player_2_playing.referee("Player 2")
    if player_2 == 0:
        print("Player 2 won!")
        exit()