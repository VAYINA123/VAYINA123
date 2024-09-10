number_to_guess = 5
user_guess = None

print("Please Enter A number From 100 To  0")
    
while user_guess != number_to_guess:
        user_guess = int(input("Enter Your Number: "))

        if user_guess < number_to_guess:
            print("The guess is too low Try Again")
        elif user_guess > number_to_guess:
            print("The Guess is too high Try Again.")
        else:
            print(f"U have Guessed The Number Correctly:{number_to_guess}.")