queue = ['Jhon','amy','bob']

queue.insert(3,'vigaca')
print(queue)


fruits=["apple", "banana", "cherry", "date",  "elderberry"]

print(fruits)

print(fruits.index("apple"))
print(fruits.index("elderberry"))

fruits.insert(5,'fig')

fruits.remove("apple")

fruits.insert(1,'blueberry')

print(len(fruits))

number = [ 10, 20, 30, 40, 50, 60, 70, 80, 90]

number.append(100)

number.insert(0,5)

number.remove(30)

number.reverse()

print(number.index(50))

print(number.count(20))

print(number)

num = [1,2,3,4,5,6,7,8,9,10]

first_half = 'numbers: {0} {1} {2} {3} {4}'. format(num[0],num[1],num[2],num[3],num[4])

second_half = 'numbers: {5} {6} {7} {8} {9}'. format(num[5],num[6],num[7],num[8],num[9])

squear = [1,4,9,16,36,49,64,81,100]

print(first_half)
print(second_half)
print(squear)


temperaturs =  [72, 68, 75, 70, 78, 74, 71]

temp = max(temperaturs)

temper = min(temperaturs)

sum = sum(temperaturs)

above_70=[70,71,72,74,75,75]
print(above_70)