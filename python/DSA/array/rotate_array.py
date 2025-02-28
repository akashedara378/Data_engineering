def reverse(arr, start, end):
    
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    return arr


def rotate_array(arr, k):
    
    n =  len(arr)
    
    k = k%n
    
    arr=reverse(arr, 0, n-1)
    
    arr=reverse(arr,0, k-1)
    
    arr=reverse(arr, k, n-1)
    
    return arr
  

# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr1, 3)  # Rotating by 3 steps
print(arr1)  # Output: [5, 6, 7, 1, 2, 3, 4]

arr2 = [-1, -100, 3, 99]
rotate_array(arr2, 2)  # Rotating by 2 steps
print(arr2)  # Output: [3, 99, -1, -100]
