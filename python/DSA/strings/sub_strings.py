def all_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])
            
    return result

# Test cases
print(all_substrings("abc"))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
print(all_substrings("xy"))   # Output: ['x', 'xy', 'y']
print(all_substrings(""))      # Output: []
print(all_substrings("a"))     # Output: ['a']
