

def merge_sorted_lists(l1,l2):
    
    l3 = []
    i, j = 0,0
    
    while i < len(l1) and i < len(l2):
        
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i +=1
        else:
            l3.append(l2[j])
            j +=1
        
    while i < len(l1):
        l3.append(l1[i])
        i +=1
        
    while j < len(l2):
        l3.append(l2[j])
        j +=1
        
    return l3




l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
result = merge_sorted_lists(l1, l2)
print("Merged sorted list:", result)
