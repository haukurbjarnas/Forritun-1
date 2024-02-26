def year_progression (input_file) -> tuple:
    """opens a file and prints its contents as a tuple"""
    file = open(input_file, "r")
    for line in file:
        year_and_month, inflation_num = line.split()
        print((str(year_and_month), float(inflation_num)))

def year_overview (input_file) -> tuple:
    """opens a file and prints a tuple of the year, first index and last index"""
    file = open(input_file, "r")
    index_list = []
    the_year = ""
    for line in file:
        we_need, we_do_not_need = line.split()
        the_year = we_need[0:4]
        index_list.append(we_do_not_need)
        break

    for line in file:
        year_month, index_num = line.split()
        if year_month[0:4] == the_year:
            index_list.append(index_num)
        else:
            print(((int(the_year)), (float(index_list[0])), (float(index_list[-1]))))
            index_list.clear()
            the_year = year_month[0:4]
            index_list.append(index_num)
    print(((int(the_year)), (float(index_list[0])), (float(index_list[-1]))))

def inflation_of_year (input_file) -> tuple:
    """Calculates the inflation of given year"""
    file = open(input_file, "r")
    index_list = []
    the_year = ""
    for line in file:
        we_need, we_do_not_need = line.split()
        the_year = we_need[0:4]
        index_list.append(we_do_not_need)
        break

    for line in file:
        year_month, index_num = line.split()
        if year_month[0:4] == the_year:
            index_list.append(index_num)
        else:
            year, inital, final = (int(the_year)), (float(index_list[0])), (float(index_list[-1]))
            inflation = ((final - inital)/inital) * 100
            print(((int(year)), (round(float(inflation), 2))))
            index_list.clear()
            the_year = year_month[0:4]
            index_list.append(index_num)
    year, inital, final = ((int(the_year)), (float(index_list[0])), (float(index_list[-1])))
    inflation = ((final - inital)/inital) * 100
    print(((int(year)), (round(float(inflation), 2))))

def main():
    """main file. takes input and calls the functions"""
    info_file = input("")
    try:
        year_progression(info_file)
        year_overview(info_file)
        inflation_of_year(info_file)
    except FileNotFoundError:
        print("")

main()