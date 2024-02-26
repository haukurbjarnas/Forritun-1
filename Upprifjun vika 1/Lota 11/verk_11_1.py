adress = "a"

adress_list = []
tuple_list = []

while adress != "q":
    adress = input()
    adress_list.append(adress)

adress_list.remove(adress_list[-1])

for ad in adress_list:
    tup = tuple(ad.split())
    tuple_list.append(tup)

print(adress_list)
print(tuple_list)