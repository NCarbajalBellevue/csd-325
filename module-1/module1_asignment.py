# Name: Natalia Carbajal
# Date: 6/7/2026
# Assignment: Module 1.3
# Purpose: Display a countdown of bottles of beer on the wall.

# This function counts down the bottles of beer and displays the song lyrics.
def recursive_numbers(n):
    if n > 1:
        print(n, "bottles of beer on the wall,", n, "bottles of beer.")
        n = n - 1
        print("Take one down and pass it around,", n, "bottle(s) of beer on the wall.")
        recursive_numbers(n)

    elif n == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottles of beer on the wall.")

# Get user input
number = int(input("How many bottles of beer are on the wall? "))

# Make sure the number is valid
while number <= 0:
    print("Number must be greater than 0.")
    number = int(input("How many bottles of beer are on the wall?"))

# Run recursive function
recursive_numbers(number)

# Return to the main program
print("Time to buy more bottles of beer.")