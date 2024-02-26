def open_file():

    a_file = input()

    try:
        file = open(a_file, "r")
    except ValueError:
        print("")
        exit()

    return file


def reading_file(file):

    name_list = list()
    stat_dict = dict()

    for line in file:
        first_name, last_name, throw = line.split(" ")

        name = first_name + " " + last_name

        splitted_throw = throw.split("\n")


        if name in name_list:

            stat_dict[name].append(float(splitted_throw[0]))
        
        else:
            stat_dict[name] = [float(splitted_throw[0])]
            name_list.append(name)

    return name_list, stat_dict

def finding_average(stat_dict):

    # checka hvort innihalda lykilsins sé meira en tveir og reikna the average
    # summa listans
    # geyma hvar? bara eitt average sem er síðan printað. variable fær nýtt value ef nýja er
    # stærra?

    average_dict = dict()
    
    for name, values in zip(stat_dict.keys(), stat_dict.values()):

        if len(values) > 1:
            average = sum(values)/len(values)

            average_dict[name] = round(average, 2)


    if len(average_dict) > 0:
        highest_average = max(average_dict.values())
    else:
        highest_average = None

    name_of_player = ""

    for key, values in zip(average_dict.keys(), average_dict.values()):

        if values == highest_average:
            name_of_player = key


    return name_of_player, highest_average


def printing_results(a_list, a_dict, name, average):


    for key, value in zip(a_dict.keys(), a_dict.values()):
        print(key, value)


                


def main():

    file = open_file()

    name_list, stat_dict = reading_file(file)

    name_of_player, highest_average = finding_average(stat_dict)

    printing_results(name_list, stat_dict, name_of_player, highest_average)




main()