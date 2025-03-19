
data = [-2, 45, 0, 11, -9]

n = len(data)

for i in range(n):
    for j in range(n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            

print(data)


# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)  # [11, 12, 22, 25, 64]
