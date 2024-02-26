yes_or_no = "y"

list_of_mails = []
the_dict = {}

list_of_mails.append("1")

while yes_or_no != "n":
    the_mail = input("")
    the_grade = float(input(""))

    for mail in list_of_mails:
        if mail == the_mail:
            the_dict[mail].append(the_grade)

    if the_mail not in list_of_mails:
        the_dict[the_mail] = [the_grade]
        list_of_mails.append(the_mail)

    yes_or_no = input("")

new_dict = sorted(the_dict)

for i in new_dict:
    the_sum = 0
    grade_list = []
    for j in the_dict[i]:
        the_sum += j
        grade_list.append(j)
    print(f"{i}: {round(the_sum/len(grade_list),2)}")