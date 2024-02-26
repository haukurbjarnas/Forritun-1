class MusicAlbum:

    def __init__(self, band="unkown band", title="unknown", year="unknown year"):

        self.band = band

        self.title = title

        self.year = year

    def set_album(self, band=None, title=None, year=None):

        if band != None:
            band = self.band
        
        if title != None:
            title = self.title

        if year != None:
            year = self.year

    def __str__(self) -> str:
        return f"Album {self.title} by {self.band}, released in {self.year}."
    

the_best_one = MusicAlbum("Silk Sonic", "An Evening with Silk Sonic", "2020")

a_classic = MusicAlbum(year="1999", title="Doggystyle")

print(a_classic)