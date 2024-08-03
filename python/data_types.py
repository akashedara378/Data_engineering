#lists
a = ['apple', 'banana', 'cherry']

a[1]

more_fruits = a + ['date', 'elderberry']  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

repeated_fruits = a * 2  # ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

fruits.append('fig')  # ['apple', 'banana', 'cherry', 'fig']
fruits.insert(1, 'blueberry')  # ['apple', 'blueberry', 'banana', 'cherry', 'fig']

fruits.remove('banana')  # ['apple', 'blueberry', 'cherry', 'fig']
last_fruit = fruits.pop()  # 'fig'; list is now ['apple', 'blueberry', 'cherry']
del fruits[2]

#comprehensions
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#nested
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_element = matrix[0][0]  # 1


#tuples :  similar to lists but are immutable.
point = (1, 2)

# unopacking
coordinates = (10, 20)
x, y = coordinates  # x = 10, y = 20


#dic

person = {'name': 'Alice', 'age': 30}

name = person['name']  # 'Alice'
age = person.get('age')  # 30

person['city'] = 'New York'  # Adds a new key-value pair

del person['age']  # Removes the key 'age' and its value
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  # Deletes the key 'b' and its associated value
print(my_dict)  # Output: {'a': 1, 'c': 3}
key, value = my_dict.popitem()  # Removes and returns the last key-value pair
print(my_dict)  # Output might be: {'a': 1, 'b': 2}
print(key, value)  # Output: 'c' 3



keys = person.keys()  # dict_keys(['name', 'city'])
values = person.values()  # dict_values(['Alice', 'New York'])
items = person.items()  # dict_items([('name', 'Alice'), ('city', 'New York')])

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)  # Output: a 1, b 2, c 3


squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

students = {
    'Alice': {'age': 22, 'major': 'CS'},
    'Bob': {'age': 24, 'major': 'Math'}
}
alice_major = students['Alice']['major']  # 'CS'

#sets: unordered and unique
unique_numbers = {1, 2, 3}
unique_numbers.add(4)  # Adds 4 to the set
unique_numbers.remove(3)  # Removes 3 from the set

is_present = 2 in unique_numbers  # True

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # {3}

difference_set = set1 - set2  # {1, 2}

sym_diff_set = set1 ^ set2  # {1, 2, 4, 5}

squares_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
