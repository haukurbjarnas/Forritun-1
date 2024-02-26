def main():
    filename = input("Enter filename: ")
    file_lines = get_file_lines(filename)
    if file_lines == None:
        print(f"File {filename} not found!")
        exit()
    movie_dict = get_movie_dictionary(file_lines)
    display_options()
    choice = int(input("Enter your selection: "))
    choices = [1, 2, 3]
    while choice in choices:
        if choice == 1:
            display_alphabetical_order(movie_dict)
        elif choice == 2:
            year = int(input("Enter year: "))
            display_titles_in_given_year(movie_dict, year)
        elif choice == 3:
            modifier = float(input())
            modify_ratings(movie_dict, modifier)
        display_options()
        choice = int(input("Enter your selection: "))





# You can use this function if you like.
def get_file_lines(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return None


# Feel free to define more functions of course.

def display_options():
    print("")
    print("\n"+"*"*31)
    print("1. Movies in alphabetical order")
    print("2. Titles in given year")
    print("3. Modify all ratings")
    print("*"*31+("\n"))


def get_movie_dictionary(filelines):
    movie_dict = dict()
    for line in filelines:
        split_line = line.split(";")
        movie_dict[split_line[0]] = [float(split_line[1]), int(split_line[2])]
    return movie_dict

def display_alphabetical_order(movie_dict):
    print("\n")
    for title in sorted(movie_dict.keys()):
        print(f"{title:<50} {movie_dict[title][0]:>6}{movie_dict[title][1]:>6}")

def display_titles_in_given_year(movie_dict, year):
    for title in movie_dict.keys():
        if movie_dict[title][1] == year:
            print(title)

def modify_ratings(movie_dict, modifier):
    for title in movie_dict.keys():
        movie_dict[title][0] += modifier

if __name__ == "__main__":
    main()
