def find_second_largest(arr):
    if len(arr) < 2:
        return "none"
        
    first = second = float('-inf')
    
    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    
    return second if second != float('-inf') else None

# Test cases
print(find_second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(find_second_largest([5, 5, 5, 5]))         # Output: None (all elements are the same)
print(find_second_largest([10, 10, 9, 8, 7]))    # Output: 9
print(find_second_largest([2]))                  # Output: None (only one element)
print(find_second_largest([100, -5, 2, 99, 100]))# Output: 99
