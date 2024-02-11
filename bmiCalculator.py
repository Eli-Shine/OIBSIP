"""Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight (kg) / (height (m) * height (m))
"""
print("Welcome to the BMI Calculator")
print("-------------------------------")

name = input("What is your name? ")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please enter correct weight and height values.")
    else:
        # Calculate BMI
        bmi = weight / (height * height)

        # Classify BMI into categories based on predefined ranges
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Print BMI and category
        print(f"Hello {name}, Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

except ValueError:
    print("Please enter valid numeric values for weight and height.")

