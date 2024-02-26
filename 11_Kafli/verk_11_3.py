def list_to_bool_tuple(test_input):
    my_list = []
    new_list = test_input.split(",")

    for i in new_list:
        if bool(i) == False:
            my_list.append(False)
        elif i == "0":
            my_list.append(False)
        else:
            my_list.append(True)
    return tuple(my_list)
