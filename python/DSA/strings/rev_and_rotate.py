# reverse
def change(a):
    x = ""
    for i in a:
        x = i + x
    return x

def rev(b):
    words = b.split()
    x = [word[::-1] for word in words]
    return " ".join(x)
a = "akash is good boy"
print(change(a))
print(rev(a))


def rotate_string(s: str, k: int, direction: str = 'left') -> str:
    n = len(s)
    
    k = k%n
    
    if direction == 'left':
        return s[k:]+s[:k]
    elif direction == 'right':
        return s[-k:]+s[:-k]
    else:
        raise ValueError("Direction must be either 'left' or 'right'.")

# Test cases
print(rotate_string("abcdef", 2, 'left'))   # Output: "cdefab"
print(rotate_string("abcdef", 2, 'right'))  # Output: "efabcd"
print(rotate_string("hello", 3, 'left'))    # Output: "lohel"
print(rotate_string("hello", 3, 'right'))   # Output: "llohe"
print(rotate_string("rotation", 5, 'left'))  # Output: "ationrot"
print(rotate_string("rotation", 5, 'right')) # Output: "tionrota"
