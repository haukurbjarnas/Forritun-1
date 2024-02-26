class MusicAlbum:

    def __init__(self, band = "unknown band", title = "unknown", year = "unknown year"):
        self.band = band
        self.title = title
        self.year = year

    def set_album (self, band = None, title = None, year = None):
        if band != None:
            band = self.band
        if title != None:
            title = self.title
        if year != None:
            year = self.year


    def __str__(self):
        return f"Album {self.title} by {self.band}, released in {self.year}."