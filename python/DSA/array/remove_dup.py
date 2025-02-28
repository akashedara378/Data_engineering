def remove_duplicates(arr):
    if not arr:
        return None
    
    i =0
    
    for j in range(1, len(arr)):
        if arr[i] == arr[j]:
            j +=1
        else:
            i +=1
            arr[i] = arr[j]
    return i+1

# Test cases
arr1 = [1, 1, 2]
new_length1 = remove_duplicates(arr1)
print(arr1[:new_length1], new_length1)  # Output: [1, 2], 2

arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length2 = remove_duplicates(arr2)
print(arr2[:new_length2], new_length2)  # Output: [0, 1, 2, 3, 4], 5

arr3 = []
new_length3 = remove_duplicates(arr3)
print(arr3[:new_length3], new_length3)  # Output: [], 0

arr4 = [1, 2, 3, 4, 5]
new_length4 = remove_duplicates(arr4)
print(arr4[:new_length4], new_length4)  # Output: [1, 2, 3, 4, 5], 5
