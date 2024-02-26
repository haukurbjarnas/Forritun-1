import string

def file_check (text_file):
    try:
        open(text_file)
    except FileNotFoundError:
        exit()

def txt_file_sorting(text_file):

    file = open(text_file, "r")

    document_dictio = dict()
    current_document_1 = 1
    document_dictio[current_document_1] = set()

    for line in file:
        if line == "<END OF DOCUMENT>\n" or line == "<END OF DOCUMENT>":
            current_document_1 += 1
            document_dictio[current_document_1] = set()
        else:
            document_dictio[current_document_1].add(line.rstrip("\n"))

    combined_dict = {}

    for key,values in document_dictio.items():
        combined_value = ' '.join(values)
        combined_dict[key] = combined_value

    

    if len(document_dictio[current_document_1]) == 0:
        del document_dictio[current_document_1]



    return combined_dict



def txt_file_sorting_word(text_file):
    
    file = open(text_file, "r")

    document_dict = dict()
    current_document = 1
    document_dict[current_document] = set()

    for line in file:
        if line == "<END OF DOCUMENT>" or line == "<END OF DOCUMENT>\n":
            current_document += 1
            document_dict[current_document] = set()
        else:
            splitted_line = line.split()
            for word in splitted_line:
                clean_word = remove_punctuation(word).lower()
                document_dict[current_document].add(clean_word)

    if len(document_dict[current_document]) == 0:
        del document_dict[current_document]
    
    return document_dict


def remove_punctuation(line):
    translator = str.maketrans('', '', string.punctuation.replace("-", ""))
    cleaned_text = line.translate(translator)
    return cleaned_text








def main():
    text_file_name = input()
    file_check(text_file_name)
    txt_file_sorting_word(text_file_name)
    command = input()
    while command != "quit":
        
        if command == "search":
            search_word = (input().lower()).split()
            set_to_search = set()
            for word in search_word:
                set_to_search.add(remove_punctuation(word))
            document_file_word = txt_file_sorting_word(text_file_name)
            key_list = []
            for key,values in document_file_word.items():
                if set_to_search.issubset(values):
                    key_list.append(int(key))

            sorted_list = sorted(key_list)
            

            if len(sorted_list) >= 1:
                print("Documents matching search:", end=" ")
                for number in key_list:
                    print(number, end=" ") 
                print()
            else:
                print("No match")

                
        
        
        if command == "print":
            document_file = txt_file_sorting(text_file_name)
            number_of_file = int(input())
            if number_of_file not in document_file:
                print("No match")
            else:
                print(f"Document #{number_of_file}:")
                for line in document_file[number_of_file]:
                    print(line)
        command = input()



main()