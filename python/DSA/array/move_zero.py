def move_zeroes(arr):
    i = 0
    
    for j in range(len(arr)):
        while arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
    return arr
# Test cases
arr1 = [0, 1, 0, 3, 12]
move_zeroes(arr1)
print(arr1)  # Output: [1, 3, 12, 0, 0]

arr2 = [0, 0, 0, 1, 2]
move_zeroes(arr2)
print(arr2)  # Output: [1, 2, 0, 0, 0]

arr3 = [1, 2, 3, 4, 5]
move_zeroes(arr3)
print(arr3)  # Output: [1, 2, 3, 4, 5] (no change since no zeroes)

arr4 = [0, 0, 0, 0]
move_zeroes(arr4)
print(arr4)  # Output: [0, 0, 0, 0] (all zeroes remain)
