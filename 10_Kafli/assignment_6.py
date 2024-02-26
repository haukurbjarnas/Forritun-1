def file_to_list (file_name):
    file_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                for i in line:
                    if ord(i) >= 48 and ord(i) <= 57:
                        file_list.append(line.replace("\n", " "))
                        break
        return file_list
    except FileNotFoundError:
        return (f"File '{file_name}' not found.")
    except Exception as e:
        return (f"An error occurred: {e}.")

def list_to_list (file_list):
    num_list = []
    for i in file_list:
        for j in i:
            if ord(j) >= 48 and ord(j) <= 57:
                number = float(i)
                num_list.append(number)
                break
    for i in num_list:
        return round(i, 4)
    return ""

def sum_process (num_list):
    sum = 0
    for i in num_list:
        sum += i
        return round(sum, 4)
    
def sorting (sorted_list):
    sorted_list =