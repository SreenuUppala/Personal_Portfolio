import pandas as pd
import matplotlib.pyplot as plt

file_name = "data.csv"

# Read CSV
data = pd.read_csv(file_name)

print("\nData Preview:")
print(data)

# User input for graph type
print("\nChoose Graph Type:")
print("1. Bar Chart")
print("2. Line Chart")
print("3. Pie Chart")

choice = input("Enter your choice: ")

# Bar Chart
if choice == "1":
    plt.bar(data["Month"], data["Sales"])
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales - Bar Chart")

# Line Chart
elif choice == "2":
    plt.plot(data["Month"], data["Sales"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales - Line Chart")

# Pie Chart
elif choice == "3":
    plt.pie(data["Sales"], labels=data["Month"], autopct="%1.1f%%")
    plt.title("Monthly Sales - Pie Chart")

else:
    print("Invalid choice")

plt.show()
