class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, film):
        self.items.append(film)

    def set_name(self, new_name):
        self.name = new_name

    def remove(self, film):
        self.items.remove(film)

    def clear(self):
        self.items.clear()

    def __str__(self):
        result = f"Catalog {self.name}:\n"
        for item in self.items:
            result += f"    {item}\n"
        return result.rstrip('\n')