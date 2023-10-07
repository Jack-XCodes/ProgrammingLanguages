#  Part B: Control Flow
# Read through the content on control flow and attempt the following code challenges.
# 3. Create A BMI Calculator app. After calculating the BMI of a person, the calculator should
# inform the person if they are underweight, Normal weight or Overweight.
# Prompt the user for their weight in kilograms
weight_kg = float(input("Enter your weight in kilograms: "))

# Prompt the user for their height in meters
height_m = float(input("Enter your height in meters: "))

# Calculate BMI (Body Mass Index)
bmi = weight_kg / (height_m ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
else:
    category = "Overweight"

# Display the BMI and category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the '{category}' category.")
