def inputs():
    amount_of_inputs = int(input())

    a_dict = dict()

    for num in range(amount_of_inputs):

        content_creator = input()
        views = int(input())

        if content_creator in a_dict:
            a_dict[content_creator] += views
        
        else:
            a_dict[content_creator] = views

    sorted_list = sorted(a_dict.items(), key=lambda item: item[1], reverse=True)
    
    name, fame = sorted_list[0]

    print(name)


blabla = inputs()

