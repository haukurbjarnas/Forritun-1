def without_outliers (a_list: list) -> list:
    new_list = []

    def find_min_and_max_index(a_list: list) -> tuple:
        """Finds the position of the lowest number and the highest number in the list."""

        min_index, max_index = 0, 0

        for i in range(1, len(a_list)):
            if a_list[i] < a_list[min_index]:
                min_index = i

            if a_list[i] > a_list[max_index]:
                max_index = i

        return min_index, max_index
    
    min_index, max_index = find_min_and_max_index(a_list)

    for digit in a_list:
        for i in range(len(a_list)-1):
            if i == min_index or max_index:
                i += 1
                break
            else:
                new_list.append(digit)
                i += 1
    
    return new_list

yes = [2, 7, 4, 1,]

hola = without_outliers(yes)

print(hola)