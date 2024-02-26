from typing import List

class Yatzee():

    def __init__(self) -> None:
        
        self.points = None

    MAX_DICE_RESULT = 6

    def get_counts(self, dice_results: List[int]) -> List[int]:
        # function from starter code
        self.dice_results = dice_results
        self.counts = [self.dice_results.count(value) for value in range(1, self.MAX_DICE_RESULT + 1)]
        return self.counts
    
    def round(self, throw):

        self.throw = throw

        self.dices_devided = self.throw.split(" ")

        self.int_dices = []

        for self.index in self.dice_results:
            self.int_dices.append(int(self.index))

        self.points_in_round = self.get_counts(self.int_dices)

        return self.points_in_round
    
    def checking_points(self, number):
        self.number = number

        self.points = 0

        for i in self.potential_points:
            if i == self.number:
                self.points = self.number * self.number
            self.number += 1
        
        for i in self.potential_points:
            if i == 5:
                return 50

        return self.points
    
    def main(self):

        self.throw = input()

        while self.throw != "[0 0 0 0 0]":

            self.potential_points = self.round(self.throw)

            self.point_2 = self.checking_points(self.potential_points, 2)

            self.point_3 = self.checking_points(self.potential_points, 3)

            if self.point_2 and self.point_3 == 50:
                return 50
            elif self.point_3 > 0:
                return self.point_3
            elif self.point_2 > 0:
                return self.point_2
            else:
                return 0



playing = Yatzee()

confirmation_of_quitting = 0

while confirmation_of_quitting == 0:
    round = playing.main()
    print(round)
