def reverse_array(arr):
    
    left = 0
    right = len(arr)-1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    
    return arr

# Test cases
print(reverse_array([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(reverse_array([10, 20, 30]))     # Output: [30, 20, 10]
print(reverse_array([7]))              # Output: [7] (single element, no change)
print(reverse_array([]))               # Output: [] (empty array, no change)
