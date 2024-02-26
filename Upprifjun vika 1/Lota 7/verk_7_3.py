def extract_first_number_from_string(string_to_search):

    for word in string_to_search.split():
        try:
            if int(word) / int(word) == 1:
                return int(word)
            break
        except ValueError:
            continue
    return -1
    
 

print(extract_first_number_from_string("365 24 days"))