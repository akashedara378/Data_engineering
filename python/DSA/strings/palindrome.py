#two pointer palandrome

def check(a: str)-> bool:
    left, right = 0, len(a)-1
    
    while left < right:
        if a[left] != a [right]:
            return False
        left +=1
        right -=1
        
    return True
a='madam'
