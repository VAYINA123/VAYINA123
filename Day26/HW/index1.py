Weight = float(input("Enter Your Weight"))
height = float(input("Enter your height"))


bmi = Weight / (height ** 2)

if   bmi <= 18.5:
    print("U are underweight")

if bmi >= 18.5 or bmi <= 25:
    print("U are Normal Weight")

if bmi >= 25 or bmi <= 30 :
    print("U are overweight")

if bmi >= 30:
    print("U are in the Obesity Category ")