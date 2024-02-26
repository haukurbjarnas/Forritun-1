def open_file():    
    movie_file = input("Enter filename: ")

    conformation = 0

    while conformation == 0:
        try:
            file = open(movie_file, "r")
            conformation += 1
        except FileNotFoundError:
            print(f"File {movie_file} not found!")
            movie_file = input("Enter filename: ")
    
    return file

def menu_of_operations():

    print("")
    print("*"*31)
    print("1. Movies in alphabetical order")
    print("2. Titles in given year")
    print("3. Modify all ratings")
    print("*"*31)
    print("")

def remove_letter(input_string, letter_to_remove):
    cleaned_string = ''.join(char for char in input_string if char != letter_to_remove)
    return cleaned_string

def from_file_to_output(file):

    conformation_list = []

    movie_dict = dict()

    for line in file:
        name, rating, year = line.split(";")

        name = remove_letter(name, ",")

        rating = remove_letter(rating, ",")

        conformation_list.append(name)

        year = remove_letter(year, "\n")


        movie_dict[name] = [rating, year]

    return sorted(conformation_list), movie_dict

file = open_file()

alphabetical_list, movie_dictionary = from_file_to_output(file)

def alphabetical_print(a_list, a_dict):
    for film in a_list:
        if film in (a_dict.keys()):
            print(f"{film:<50s} {a_dict[film][0]:>6s} {a_dict[film][1]:>6s}")

def search_by_given_year(a_list, a_dict):

    a_year = (input("Enter year: "))

    for year, film in zip(a_dict.values(), a_list):

        if a_year == a_dict[film][1]:
            print(film)

search_by_given_year(alphabetical_list, movie_dictionary)