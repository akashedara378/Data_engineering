def find_pair_with_sum(arr, target):
    
    dict1 = {}
    
    for i, num in enumerate(arr):
        x = target - num
        
        if x in dict1:
            return x, num
        else:
            dict1[num] = i
    print(dict1)
    return None
    
arr1 = [2, 7, 11, 15]
target1 = 9
print(find_pair_with_sum(arr1, target1))  # Output: (2, 7)

arr2 = [3, 2, 4]
target2 = 6
print(find_pair_with_sum(arr2, target2))  # Output: (2, 4)

arr3 = [3, 3]
target3 = 6
print(find_pair_with_sum(arr3, target3))  # Output: (3, 3)

arr4 = [1, 2, 3, 4, 5]
target4 = 10
print(find_pair_with_sum(arr4, target4)) 
