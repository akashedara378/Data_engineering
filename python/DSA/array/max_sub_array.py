# kadane's algorithm

def max_subarray(nums):
    current_sum = 0
    max_sum = float("-inf")
     
    for num in nums:
        
        current_sum = max(num, current_sum+num)
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr1))  # Output: 6 (subarray: [4, -1, 2, 1])

arr2 = [1]
print(max_subarray(arr2))  # Output: 1

arr3 = [-1, -2, -3]
print(max_subarray(arr3))  # Output: -1 (best single element subarray)

arr4 = [5, 4, -1, 7, 8]
print(max_subarray(arr4))  # Output: 23 (subarray: [5, 4, -1, 7, 8])
