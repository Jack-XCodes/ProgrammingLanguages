
# 2. Create a tip calculator that takes in the total bill amount, the tip amount as a percentage of
# the total bill amount (10,12 or 15 should be the options) and the number of people
# splitting the bill. After getting these user input values your app should calculate the
# amount each person should pay and display the answer rounded to two decimal points

# Prompt the user for the total bill amount
total_bill = float(input("Enter the total bill amount: $"))

# Prompt the user for the tip percentage (10%, 12%, or 15%)
while True:
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    if tip_percentage in [10, 12, 15]:
        break
    else:
        print("Invalid input. Please choose 10, 12, or 15 for tip percentage.")

# Prompt the user for the number of people splitting the bill
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip amount
tip_amount = (tip_percentage / 100) * total_bill

# Calculate the total amount to be paid including the tip
total_amount = total_bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_amount / num_people

# Display the result rounded to two decimal points
print(f"Each person should pay: ${amount_per_person:.2f}")
