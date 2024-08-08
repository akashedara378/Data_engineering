
#max sum conseqyent
def max_sub(a):
    
    max_global = max_current = a[0]
    
    for i in range(1, len(a)):
        max_current = max( max_current, a[1]+max_current)
        
        if max_current > max_global:
            max_global = max_current
        
    return max_global





a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
b = max_sub(a)
print(b)



def largest_sum_of_two_elements(lst):
    # Check if the list has fewer than two elements
    if len(lst) < 2:
        return "List must contain at least two elements."
    
    # Sort the list in descending order
    lst_sorted = sorted(lst, reverse=True)
    
    # Sum the first two elements in the sorted list
    largest_sum = lst_sorted[0] + lst_sorted[1]
    
    return largest_sum

# Example usage
example_list = [10, 5, 12, 7, 9]
result = largest_sum_of_two_elements(example_list)
print("The largest sum of any two elements in the list is:", result)


print(sorted(a, reverse=True))
