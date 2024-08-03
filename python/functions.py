# functions_and_lambda.py

# Functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def person(name, age=30):
    return f"{name} is {age} years old."

def sum_numbers(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Scope
global_var = "I am global"

def local_scope_example():
    local_var = "I am local"
    print(local_var)

def global_scope_example():
    print(global_var)

# Lambda Expressions
add_lambda = lambda x, y: x + y
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))
even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
sorted_pairs = sorted([(1, 'one'), (3, 'three'), (2, 'two')], key=lambda x: x[1])

# Output Results
print("Function Examples:")
print(greet("Alice"))                # Hello, Alice!
print(add(5, 3))                    # 8
print(person("Bob"))                # Bob is 30 years old.
print(person("Bob", 25))           # Bob is 25 years old.
print(sum_numbers(1, 2, 3, 4))     # 10
print_info(name="Alice", age=30)   # name: Alice \n age: 30

print("\nScope Examples:")
local_scope_example()              # Output: I am local
global_scope_example()             # Output: I am global

print("\nLambda Expressions:")
print(add_lambda(5, 3))            # 8
print(squared)                     # [1, 4, 9, 16]
print(even_numbers)                # [2, 4]
print(sorted_pairs)                # [(1, 'one'), (2, 'two'), (3, 'three')]
