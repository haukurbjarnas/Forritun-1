class Kvedjuparty:

    def __init__(self, boysar) -> None:
        
        self.boysar = boysar

    def what_to_drink(self):

        sum = 1

        for key in self.boysar.keys():

            print(f'{sum}. {key}')

            sum += 1

        drinker = input('Enter name of drinker: ')

        drink = ''

        while drink != 'q':

            drink = input(f'Enter drink for {drinker}: ')

            self.boysar[drinker].append(drink)

    def __str__(self) -> str:
        
        for key, elem in self.boysar.items():

            print(f'{key}', end=' ')

            for drink in elem:
                print(drink, end=', ')


ja = Kvedjuparty({'Haukur':[], 'Smári':[], 'Óliver':[], 'Bárður':[], 'Ægir':[], 'Hjalti':[]})

while True:

    print('1. Enter drink!')
    print('2. Drink drink!')
    print('3. View all drinks!')

    command = input('Enter action: ')

    if command == '1':
        ja.what_to_drink()
    elif command == '2':
        pass
    elif command == '3':
        print(ja)
    elif command == 'q':
        exit()
    else:
        print('Invalid input!')