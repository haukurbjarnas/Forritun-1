from typing import List


def extract_evens(int_list: List[int]) -> List[int]:
    only_odd = []
    for i in int_list:
        if int(i) % 2 == 0:
            only_odd.append(i)
    return only_odd




def remove_odds(int_list: List[int]) -> None:

    new_list = []

    for digit in int_list:
        if int(digit) % 2 == 0:
            new_list.append(digit)
    int_list.clear()

    int_list.extend(new_list)