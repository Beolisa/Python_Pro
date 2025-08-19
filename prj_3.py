nHeight = float(input("Enter your height in kilogram: "))
nWeight = int(input("Enter your weight in centimeter: "))

BMI = nWeight / (nHeight ** 2)

if (BMI < 18.5):
    print("Under weight.")
elif (18.5 <= BMI <= 24.9):
    print("Normal.")
elif(25 <= BMI <= 29.9):
    print("Over weight.")