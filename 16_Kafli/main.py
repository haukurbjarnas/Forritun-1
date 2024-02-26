from item import Item
from catalog import Catalog

the_best = Item("The Hangover", "Comedy")

great_success = Item("Borat", "Comedy")

dorsia = Item("American Psycho", "Black comedy")

print(the_best)
print(great_success)
print(dorsia)

dorsia.set_name("OK")
dorsia.set_category("YEEEES")

catalog = Catalog("Films")

catalog.add(the_best)
catalog.add(great_success)
catalog.add(dorsia)

print(catalog)

catalog.remove(dorsia)

print(catalog)

catalog.set_name("Góðan og blessaðan")

print(catalog)

catalog.clear()

print(catalog)