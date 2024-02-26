info_file = input("")
check = 0
while check < 1:
    try:
        file = open(info_file, "r")
        check += 1
    except FileNotFoundError:
        print(f"File {info_file} not found!")
        info_file = input("")

the_dict = {}

length_list = []
length_list.append(0)

for line in file:
    if len(line)-1 in length_list:
        the_dict[len(line)-1].append(line.replace("\n",""))
    else:
        the_dict[len(line)-1] = [line.replace("\n","")]
        length_list.append(len(line)-1)

the_dict[8].append("Zimbabwe")

yes_or_no = "y"

while yes_or_no != "n":
    try:
        a_list = []
        country_search = int(input(""))
        print(", ".join(the_dict[country_search]))
    except KeyError:
        print(f"No country name of length {country_search} exists.")
    except ValueError:
        print(f"No country name of length {country_search} exists.")
    yes_or_no = input("")