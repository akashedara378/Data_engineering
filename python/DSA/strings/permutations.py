def permutations(s: str) -> list:
    if len(s) == 0:
        return [""]

    perm_list = []
    
    for i in range(len(s)):
        current_char = s[i]
        
        remaining_char = s[:i] + s[i+1:]
        
        for j in permutations(remaining_char):
            perm_list.append(current_char + j)
    
    return perm_list
# Test cases
print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(permutations("ab"))   # Output: ['ab', 'ba']
print(permutations(""))      # Output: ['']
print(permutations("a"))     # Output: ['a']
