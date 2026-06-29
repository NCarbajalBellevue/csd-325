import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    lows = []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        highs.append(int(row[5]))
        lows.append(int(row[6]))

choice = ""

while choice != "3":

    print("\nWeather Menu")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        fig, ax = plt.subplots()
        ax.plot(dates, highs, c="red")

        plt.title("Daily High Temperatures - 2018")
        plt.xlabel("")
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)")

        plt.show()

    elif choice == "2":

        fig, ax = plt.subplots()
        ax.plot(dates, lows, c="blue")

        plt.title("Daily Low Temperatures - 2018")
        plt.xlabel("")
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)")

        plt.show()

    elif choice == "3":

        print("Exiting Program! Have a nice day!")

    else:

        print("Invalid choice. Try again.")