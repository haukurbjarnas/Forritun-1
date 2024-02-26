def basics():
    
    file = open("countries.txt", "r")

    return file

def search(search_word):
    
    amount = 0

    for line in basics():
        
        if search_word in line:
            print(line, end="")
            amount += 1

    return amount
    
def main():

    search_word = input()

    amount_of_countries = search(search_word)

    print(f"{amount_of_countries} countries with suffix {search_word} in total.")

main()