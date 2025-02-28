def count_and_compress(s: str) -> str:
    if not s:
        return "null"
    
    op = []
    count =1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            op.append(s[i-1])
            op.append(str(count))
            count =1
    op.append(s[-1])
    op.append(str(count))
    return "".join(op)
    

# Test cases
print(count_and_compress("aaabbbccdaa"))  # Output: "a3b3c2d1a2"
print(count_and_compress("abcd"))         # Output: "a1b1c1d1"
print(count_and_compress(""))              # Output: ""
print(count_and_compress("a"))             # Output: "a1"
