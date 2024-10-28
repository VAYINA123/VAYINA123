def count_words(text):
words = text.split()
return len(words)


number = float(input("შეიყვანეთ რიცხვი: "))

if number > 0:
print("რიცხვი არის დადებითი.")
elif number < 0:
print("რიცხვი არის უარყოფითი.")
else:
print("რიცხვი არის ნულოვანი.")


age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age < 0:
print("Invalid ასაკი.")
elif age <= 12:
print("თქვენი ხართ  ბავშვი.")
elif age <= 17:
print("თქვენი ხართ მოზარდი.")
elif age <= 64:
print("თქვენი ხართ მოზრდილი.")
else:
print("თქვენი ხართ  მოხუცი.")


def separate_even_odd(numbers):
even_numbers = []
odd_numbers = []
    
for number in numbers:
if number % 2 == 0:
even_numbers.append(number)
else:
odd_numbers.append(number)
return even_numbers, odd_numbers