

a = " I am Working in Ericsson."


print(a [::-1])

b = ""

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string(a))

# for i reversed(a):
#     print(i)
b = ""  
for i in range(len(a), 0, -1):
    b = b + a[i-1]
    
print(b)


def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:]) + s[0]
        
print(rev("akash"))


def rev1(s):
    words = s.split()
    return "".join(words[::-1])
    
    
    
print(rev1("this is akash speaking"))

a= "this is akash speaking"
print(a[::-1])



#single occurrence

def single_oc(s):
    
    dict1 = {}
    
    for i in s:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i]=1
            
    for i in dict1:
        if dict1[i] == 1:
            print(i)

single_oc("This is akash speaking")
        
        
