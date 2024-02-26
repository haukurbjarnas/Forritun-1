yes_or_no = "y"

my_dict = {}

while yes_or_no != "n":
    the_word = input("")
    the_description = input("")
    my_dict[the_word] = the_description
    yes_or_no = input("")

sorted_dict = dict(sorted(my_dict.items()))

for item in sorted_dict:
    print(f"\n{item}:")
    print(f"    {my_dict[item]}")