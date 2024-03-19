def calculate_bmi(weight, height):
    # Convert weight to kilograms and height to meters
    weight_kg = weight
    height_m = height / 100  # Convert height from centimeters to meters
    
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    # Get user input for weight and height
    weight = int(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Print the result
    print("Your BMI is:", round(bmi, 2))

if __name__ == "__main__":
    main()
