def count_items(item_list, item):
    return item_list.count(item)

def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def average_of_list(num_list):
    total = sum(num_list) 
    return total / count if count > 0 else 0  

def reverse_list(items):
    reversed_list = []
    for item in items:
        reversed_list.insert(0, item)  
    return reversed_list