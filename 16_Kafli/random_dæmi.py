import random

# List of mathematics problems
math_problems = [
    "Problem 1: Solve for x: 2x + 5 = 15",
    "Problem 2: Calculate the area of a triangle with base 6 and height 8",
    "Problem 3: Find the square root of 25",
    "Problem 4: Compute 3 squared",
    "Problem 5: What is 12 divided by 4?",
    "Problem 6: Evaluate 7 + 9"
]

# List of people (you can customize this with names)
people = ["Haukur", "Kristján", "Máni"]

# Initialize dictionaries to store assignments for each person
assignments = {person: [] for person in people}

# Shuffle the list of math problems
random.shuffle(math_problems)

# Assign problems to people
for i, problem in enumerate(math_problems):
    person = people[i % len(people)]  # Use modulo to cycle through people
    assignments[person].append(problem)

# Print the assignments
for person, assigned_problems in assignments.items():
    print(f"{person} has the following math problems:")
    for problem in assigned_problems:
        print(problem)
    print()
