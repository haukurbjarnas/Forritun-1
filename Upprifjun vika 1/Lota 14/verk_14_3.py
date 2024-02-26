def inputs():

    yes_or_no = ""
    mail_grade = dict()

    #asking the user for the mail and the grade until the input is "n"
    while yes_or_no != "n":

        e_mail = input()
        grade = float(input())
        
        if e_mail in mail_grade:
            mail_grade[e_mail].append(grade)
        else:
            mail_grade[e_mail] = [grade]

        yes_or_no = input()

    return mail_grade

def result_of_grade(a_dict):

    for key, value in zip(a_dict.keys(), a_dict.values()):
        sum = 0

        for num in value:
            sum += num

        print(f"{key}: {round(sum / len(value), 2)}")

the_dictionary = inputs()

result_of_grade(the_dictionary)