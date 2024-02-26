a_list = ["já", "nei", "okei"]

print(type({word:word.upper() for word in a_list}))

print(type({word.upper() for word in a_list}))

print(type(set([word.upper() for word in a_list])))

