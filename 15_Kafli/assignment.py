
def main():
    text_file = input()

    print(txt_file_sorting(text_file))


def txt_file_sorting (text_file):
    try:
        file = open(text_file, "r")
    except FileNotFoundError:
        exit()

    document_dictio = dict()
    current_document = 1
    document_dictio[f"Document #{current_document}"] = []


    for line in file:
        if "<END OF DOCUMENT>" in line:
            current_document += 1
        else:
            document_dictio[f"Document #{current_document}"].append(line.rstrip("\n"))
    return document_dictio

main()