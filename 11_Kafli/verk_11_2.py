def list_to_int_tuple(search_list: list) -> tuple:
    my_list = []

    for line in search_list:
        try:
            line_int = int(line)
            my_list.append(line_int)
        except:
            ValueError
    
    return tuple(my_list)
