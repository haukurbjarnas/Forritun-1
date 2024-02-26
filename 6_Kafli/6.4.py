the_string = input("")

for i in the_string:
    if i >= "a":
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")