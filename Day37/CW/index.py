msg = input("Input a message: ")

result = msg.replace("#", " ")

print(result)

name = input('please enter your name:')
age = input('Enter your age:')

santence = 'Hello, {name}! You are {age} years old.'.format(name=name, age=age)

print(santence)

words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)

sentence = input("Input a sentence: ")

result_1 = sentence.split(" ")

print(result_1)

sentence = input("Input a sentence: ")

result = sentence.split(" ")

print(result)

mixed_case = "HeLlo WoRLd"

result = mixed_case.lower()

print(result)

convert = input("Text to convert into uppercase: ")

result = convert.upper()

print(result)