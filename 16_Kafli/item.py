class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def set_name(self, film_name):
        self.name = film_name

    def set_category(self, category_name):
        self.category = category_name

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}"