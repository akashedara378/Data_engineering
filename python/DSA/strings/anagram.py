def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    char1, char2 = {}, {}
    
    for i in s1:
        char1[i] = char1.get(i,0)+1
    
    for j in s2:
        char2[j] = char2.get(j,0)+1
        
    return char1==char2  #len(char1)==len(char2)

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False


def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    char1 = {}
    
    for i in s1:
        char1[i] = char1.get(i,0)+1
    
    for j in s2:
        char1[j] = char1.get(j,0)-1
        
    for value in char1.values():
        if value != 0:
            return False
    
    return True  #len(char1)==len(char2)

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False
