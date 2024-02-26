from typing import List

MAX_DICE_RESULT = 6

def get_counts(dice_results: List[int]) -> List[int]:
    # function from starter code
    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts


def round(results_from_throw):

    dices_divided = results_from_throw.split(" ")

    int_dices = []

    for index in dices_divided:
        int_dices.append(int(index))

    points_in_round = get_counts(int_dices)

    return points_in_round




def two_matching_dices(throw_round):
    number_of_dice = 1

    result_list = []

    for i in throw_round:
        if i == 2:
            result_list.append(2 * number_of_dice)
        number_of_dice += 1

    if len(result_list) > 0:
        return result_list[len(result_list)-1]
    else:
        return 0


def three_matching_dices(throw_round):
    number_of_dice = 1

    result_list = []

    for i in throw_round:
        if i == 3:
            result_list.append(3 * number_of_dice)
        number_of_dice += 1

    if len(result_list) > 0:
        return result_list[len(result_list)-1]
    else:
        return 0

def yatzee(throw_round):

    for i in throw_round:
        if i == 5:
            return 50
    else:
        return 0



def main():

    throw = input()

    while throw != "0 0 0 0 0":
        points_in_round = round(throw)

        check_2 = two_matching_dices(points_in_round)

        check_3 = three_matching_dices(points_in_round)

        check_5 = yatzee(points_in_round)

        if check_2 > 0 and check_3 == 0 and check_5 == 0:
            print(check_2)
        elif check_2 == 0 and check_3 > 0 and check_5 == 0:
            print(check_3)
        elif check_2 == 0 and check_3 == 0 and check_5 > 0:
            print(check_5)
        else:
            print(0)

        throw = input()

main()