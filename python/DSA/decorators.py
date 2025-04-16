import time

# Decorator function
def timer_decorator(func):
    def wrapper():
        start_time = time.time()  # Record start time
        func()  # Call the original function
        end_time = time.time()  # Record end time
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

# Function to be decorated
@timer_decorator
def say_hello():
    print("Hello, World!")
    time.sleep(1)  # Simulate a delay of 1 second

# Calling the decorated function
say_hello()
