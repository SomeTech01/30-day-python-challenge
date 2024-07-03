"""Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?"""
hours = int(input('How many hours have you worked?'))
rate = int(input('What is your hourly rate?'))
weekly = hours * rate
print(f'Your are expected to get {weekly} this week!')
print()
"""Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years"""

years = int(input('Number of years you expect to live?'))
year_to_second = 31556952
seconds = years * year_to_second
print(f"You are expected to live for {seconds} seconds!")
print()
"""Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
print()
# Function to generate the table
def generate_table(rows):
    for i in range(1, rows + 1):
        print(f"{i} 1 {i} {i**2} {i**3}")

# Number of rows you want in the table
rows = 5

# Generate and print the table
generate_table(rows)
