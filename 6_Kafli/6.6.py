the_string = input("")
lastname, firstname = the_string.split()
real_lastname = lastname[0:-1]



print("{}. {}".format(firstname[0].upper(), real_lastname.capitalize()))