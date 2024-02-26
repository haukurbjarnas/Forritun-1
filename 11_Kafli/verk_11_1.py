def tup_convert (adress):
    street, number = adress.split()
    return street, number

def main():
    tup_list = []
    norm_list = []

    home = input("")


    while home != "q":
        func_add = tup_convert(home)
        tup_list.append(func_add)
        norm_list.append(home)
        home = input("")
    
    print(norm_list)
    print(tup_list)

main()