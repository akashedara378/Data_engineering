def longest_substring_without_repeating(s: str) -> int:
    char_set = set()
    left = 0
    right = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        
        char_set.add(s[right])
        w = right-left+1
        max_len = max(max_len, w)
    
    return max_len

# Test cases
print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
print(longest_substring_without_repeating("bbbbb"))     # 1 ("b")
print(longest_substring_without_repeating("pwwkew"))    # 3 ("wke")
print(longest_substring_without_repeating(""))          # 0 (empty string)


#for getting string
def longest_substring_without_repeating(s: str) -> int:
    char_set = set()
    left = 0
    right = 0
    max_len = 0
    start_index = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        
        char_set.add(s[right])
        w = right-left+1
        
        if w > max_len:
            max_len = w
            start_index = left
    
    return s[start_index:start_index+max_len]

# Test cases
print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
print(longest_substring_without_repeating("bbbbb"))     # 1 ("b")
print(longest_substring_without_repeating("pwwkew"))    # 3 ("wke")
print(longest_substring_without_repeating(""))          # 0 (empty string)

