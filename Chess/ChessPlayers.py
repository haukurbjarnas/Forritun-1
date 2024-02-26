import csv 

class ChessPLayers:
    def __init__(self, filename):
        self.players = self._read_chess_data(filename)

    
    
    def _read_chess_data(self, filename):
        '''
            This method reads data from a csv file
            and returns the data 
        '''

        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            players = {}

            for row in reader:
                rank = row[0].strip()
                full_name = row[1].strip()
                country = row[2].strip()
                rating = row[3].strip()
                birth_year = row[4].strip()

                last_name, first_name = map(str.strip, full_name.split(","))

                players[full_name] = {
                    "rank": rank,
                    "last_name": last_name,
                    "first_name": first_name,
                    "country": country,
                    "rating": rating,
                    "birth_year": birth_year
                }

        return players
    
    def get_player_data(self, name):
        '''returns player data '''
        return self.players.get(name, None)

    def display_player_data(self, name):
        data = self.get_player_data(name)
        '''displays player data'''
        return data