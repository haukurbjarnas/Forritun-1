the_string = input("")

land_file = "countries.txt"

try:
    with open(land_file, "r") as file:
        line_sum = 0
        for line in file:
            if the_string in line:
                print(line.strip())
                line_sum += 1
        print(f"{line_sum} countries with suffix {the_string} in total.")

except FileNotFoundError:
    print(f"File '{land_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")