name = input('please enter your name:')
place = input('please enter a place:')


temple = "hello  {name}. welcome to {place}.".format(name = name,place = place)

print(temple)

shop = ['apple','bannana','cherry']

fruit_string = "," " ". join(shop)

print(fruit_string)

sentance = "The quick brown fox jumps over the lazy dog."

words_list = sentance.split(" ")

print(words_list)

quout = "To be or not to be, that is the question."

modified_code = quout.replace("be","code")

print(modified_code)

mixed_case = "PyThOn Is AwEsOmE!"

lowercase_str = mixed_case.lower()

print(lowercase_str)


gretting = "good morning"

upercase_gretting = gretting.upper()

print(upercase_gretting)