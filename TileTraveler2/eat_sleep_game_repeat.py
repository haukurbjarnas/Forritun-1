from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)

global_variable = 0



def main():
    gamer = "y"
    while gamer == "y":
        location = STARTING_LOCATION
        while location != FINAL_DESTINATION:
            location = play_one_move(location)

        print(f"Victory! Total coins {len(coin_sum)}.")
        gamer = input("Play again (y/n): ").lower()
        coin_sum.clear()

def has_lever(location):
    if location == (1, 1):
        return False
    elif location == (1, 2):
        return True
    elif location == (1, 3):
        return False
    elif location == (2, 1):
        return False
    elif location == (2, 2):
        return True
    elif location == (2, 3):
        return True
    elif location == (3, 2):
        return True
    elif location == (3, 3):
        return False


def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """
    global has_lever
    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:

        location = move(direction, location)
        checker = has_lever(location)
        if checker == True:
            question = input("Pull a lever (y/n): \n").lower()
            coin_check(question)
    else:
        print("Not a valid direction!")

    return location

coin_sum = []
def coin_check (question):
    if question == "y":
        coin_sum.append(1)
        print(f"You received 1 coin, your total is now {len(coin_sum)}.")
    if question == "n":
        pass



def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""
    global has_lever
    if location == (1, 1):
        valid_directions = (NORTH)
    elif location == (1, 2):
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        valid_directions = EAST, WEST
    elif location == (3, 2):
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    return input("Direction:\n").lower()


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y


if __name__ == "__main__":
    main()
