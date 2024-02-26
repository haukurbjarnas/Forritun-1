def main():
    file_name = input("")
    try:
        with open(file_name, "r") as file:
            for line in file:
                reversed_line = reverse_words_in_line(line)
                print(reversed_line)
    
    except FileNotFoundError:
        print("File not found")

def reverse_words_in_line(line):
    words = line.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == "__main__":
    main()