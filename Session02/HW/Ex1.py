mass = int(input("What is your weight?(kg)"))
heightincm = int(input("What is your height?(cm)"))

heightinm = heightincm/100

BMI = mass / (heightinm * heightinm)

if BMI < 16:
    print("Severly underweight")
elif BMI  > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
elif BMI > 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")