class MaxStack:
    
    def __init__(self):
        self.stack2 = []
        self.stack1 = []
        
    def push(self, val):
        self.stack1.append(val)
        if not self.stack2 or val >= self.stack2[-1]:
            self.stack2.append(val)
        
    def get_max(self):
        return self.stack2[-1] if self.stack2 else None
        
    def pop(self):
        if not self.stack1:
            return None
        val = self.stack1.pop()
        if val == self.stack2[-1]:
            self.stack2.pop()
        return val

s = MaxStack()
s.push(5)
s.push(1)
s.push(10)
s.push(3)
print(s.get_max())  # Output: 10
s.pop()
print(s.get_max())  # Output: 10
s.pop()
print(s.get_max())  # Output: 5
