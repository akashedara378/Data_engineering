def merge(arr1, arr2, m, n):
    
    i = m-1
    j = n-1
    k = m+n-1
    
    while i >=0 and j>=0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -=1
            k -=1
        else:
            arr1[k] = arr2[j]
            j -=1
            k -=1
    
    while j>=0:
        arr1[k] = arr2[j]
        j -=1
        k -=1
    
    return arr1
# Test case
arr1 = [1, 3, 5, 0, 0, 0]  # Array with extra space
arr2 = [2, 4, 6]
m = 3  # Number of valid elements in arr1
n = 3  # Number of elements in arr2

merge(arr1, arr2, m, n)
print(arr1)  # Output: [1, 2, 3, 4, 5, 6]


#without extra 00:
def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    
    l3 = [0]*(m+n)
    
    i,j,k=0,0,0
    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            l3[k] = arr1[i]
            i +=1
            k +=1
        else:
            l3[k] = arr2[j]
            j +=1
            k +=1
    
    while i < m:
        l3[k] = arr1[i]
        i +=1
        k +=1
        
    while j < n:
        l3[k] = arr2[j]
        j +=1
        k +=1
    
    return l3
# Test case
arr1 = [1, 3, 5]  # Array with extra space
arr2 = [2, 4, 6]
m = 3  # Number of valid elements in arr1
n = 3  # Number of elements in arr2

l3 = merge(arr1, arr2)
print(l3)  # Output: [1, 2, 3, 4, 5, 6]
