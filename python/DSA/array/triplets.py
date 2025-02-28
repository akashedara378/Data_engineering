def three_sum(nums):
    nums.sort()
    result = []
    n=len(nums)
    
    for i in range(n-2):
        
        if i > 0 and nums[i]==nums[i-1]:
            continue
        
        left , right = i+1, n-1
        
        while left < right:
            total = nums[left]+nums[right]+nums[i]
            
            if total == 0:
                result.append([nums[left], nums[right], nums[i]])
                left +=1
                right -=1
            
                while left < right and nums[left] == nums[left-1]:
                    left +=1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
            
            elif total <0:
                left +=1
            else:
                right -=1
                
    return result
            
            

# Test cases
arr1 = [-1, 0, 1, 2, -1, -4]
arr2 = [0, 0, 0, 0]
arr3 = [1, 2, -2, -1]

print(three_sum(arr1))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum(arr2))  # Output: [[0, 0, 0]]
print(three_sum(arr3))  # Output: []
