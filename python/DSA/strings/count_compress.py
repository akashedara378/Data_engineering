def count_and_compress(s):
    l1 = []
    count = 1
    
    for i in range(1, len(s)):
        
        if s[i] == s[i-1]:
            count +=1
        else:
            l1.append(s[i-1])
            l1.append(str(count))
            count = 1
        
    
    l1.append(s[-1])
    l1.append(str(count))
  
    return "".join(l1)

# Test cases
print(count_and_compress("aaabbbccdaa"))  # Output: "a3b3c2d1a2"
print(count_and_compress("abcd"))         # Output: "a1b1c1d1"
print(count_and_compress(""))              # Output: ""
print(count_and_compress("a"))             # Output: "a1"
