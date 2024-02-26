fullname = input()

lastname, firstname = fullname.split()

print(f"{firstname[0].upper()}. {lastname[0].upper()}{lastname[1:]}")