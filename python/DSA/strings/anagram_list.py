def group_anagrams(strs: list) -> list:
  
  dict1 = {}
  
  for s in strs:
      
      key = "".join(sorted(s))
      
      if key not in dict1.keys():
          dict1[key] = []
      dict1[key].append(s)
  
  return list(dict1.values())

# Test cases
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""]))  
# Output: [['']]
print(group_anagrams(["a"])) 
# Output: [['a']]
print(group_anagrams(["a", "b", "c", "d", "e"])) 
# Output: [['a'], ['b'], ['c'], ['d'], ['e']]
