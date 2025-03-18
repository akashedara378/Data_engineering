def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char,0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char  
    
    return None


# Test cases
print(first_non_repeating_char("leetcode"))  # "l"
print(first_non_repeating_char("loveleetcode"))  # "v"
print(first_non_repeating_char("aabb"))  # None (no non-repeating character)

#first non repeating character
def first_non_repeating_char(s: str) -> str:
    dict1 = {}
    
    for i in s:
        dict1[i] = dict1.get(i, 0)+1
    
    for char in s:
        if dict1[char] == 1:
            return char
    
    return "nothing"

# Test cases
print(first_non_repeating_char("leetcode"))  # "l"
print(first_non_repeating_char("loveleetcode"))  # "v"
print(first_non_repeating_char("aabb"))  # None (no non-repeating character)


