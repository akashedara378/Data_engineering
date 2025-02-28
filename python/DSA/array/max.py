
def maxi(l1: list) -> int:
    max1 = l1[0]
    i=1
    while i < len(l1):
        if l1[i] > max1:
            max1 = l1[i]
        i +=1
    return max1



print(maxi([1,14,2,3,5,24,0]))
