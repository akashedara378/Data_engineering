def all_substrings(s: str) -> list:
    substrings = []
    length = len(s)
    
    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(s[i:j])
            
    return substrings

# Test cases
print(all_substrings("abc"))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
print(all_substrings("xy"))   # Output: ['x', 'xy', 'y']
print(all_substrings(""))      # Output: []
print(all_substrings("a"))     # Output: ['a']
