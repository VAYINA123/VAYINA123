print("The driving program validation")

age = int(input("Enter Your Age: "))
while age <= 0:
    print("please enter a valid number of your age.")
    age = int(input("Enter Your Age: "))

driving_experience = int(input("How many years have u been driving a car: "))
while driving_experience < 0:
    print("Please Enter A valid Number.")
    driving_experience = int(input("How many years have u been driving a car "))

if age >= 18:
    if driving_experience >= 1:
        print("U can have a driving lisence")
    else:
        print("U dont have enough driving Experiene")
else:
    print("U cant have a driving licsence because u are underage.")