# // decorators :  decorator in Python is a function that takes another function and extends its behavior without explicitly modifying it. 
# //   Decorators allow you to add functionality to an existing function in a clean, readable way.
def dec_akash(func):
    def inner():
        print("going to decorate akash function")
        func()
    return inner

@dec_akash
def akash():
    print("Akash")
    

akash()

# iterators: An object that implements both __iter__() and __next__() methods.
# Iterable: An object that implements the __iter__() method and returns an iterator. Common iterables include lists, tuples, and strings.

numbers = [1, 2, 3]
iterator = iter(numbers)  # Get an iterator from the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration


#iterator
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Use the Countdown iterator
countdown = Countdown(5)
for number in countdown:
    print(number)


# custom iterators
class Fib:
    def __init__(self):
        self.a , self.b = 0,1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        a, self.a , self.b = self.a, self.b, self.a+self.b
        return a


fib = Fib()


for _ in range(10):
    print(next(fib))

#generators
# A generator is a special type of iterator created using a function that contains one or more yield statements. 
# Lazy Evaluation: Generators produce values on-the-fly and only compute them as needed, which makes them memory-efficient for large datasets.

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Iterate over the generator
for value in gen:
    print(value)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Use the generator
for number in fibonacci(5):
    print(number)


