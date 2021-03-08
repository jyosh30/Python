# BMI Calculation
Weight = int(input("Enter the weight : "))  # weight in Kgs
Height = int(input("Enter the Height in cms :"))  # Height in centimeters
Height = Height / 100  # converting cms into metres
BMI = Weight / (Height * Height)
print(float(BMI))

if BMI < 16.0:
    print("Severly Underweight")
elif BMI >= 16.0 and BMI <= 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 25.0:
    print("Your weight is normal")
elif BMI >= 25.0 and BMI <= 30:
    print("Overweight")
elif BMI >= 30.0 and BMI <= 40:
    print("More Obese")
    print("Reduce your food intake")
else:
    pass






