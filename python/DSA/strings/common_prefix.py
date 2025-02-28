#common prefix
def longest_common_prefix(strs) -> str:
    if not strs:
        return ""
        
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            
            if not prefix:
                return "no common prefix"
    
    return prefix
            
# Test cases
print(longest_common_prefix(["flower","flow","flight"]))  # "fl"
print(longest_common_prefix(["dog","racecar","car"]))     # ""
print(longest_common_prefix(["interspecies","interstellar","interstate"]))  # "inters"
