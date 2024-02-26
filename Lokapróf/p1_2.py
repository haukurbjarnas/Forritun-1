from typing import List

MAX_DICE_RESULT = 6

def get_counts(dice_results: List[int]) -> List[int]:
    # function from starter code
    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts

class Points:

    def __init__(self, a_list, points):

        self.a_list = a_list
        self.points = points

    def checking_points(self):
        self.number = 0

        self.points = 0

        for i in self.a_list:
            if i == self.number:
                self.points = self.number * self.number
            self.number += 1
        
        for i in self.a_list:
            if i == 5:
                return 50

        return self.points
    
    def __str__(self):
        
        return f"{self.points}"
    
    





def main():

    throw = input()

    while throw != "[0 0 0 0 0]":

        potential_points = round(throw)

        points_class = Points(potential_points, 2)

        print(points_class)

        throw = input()

main()