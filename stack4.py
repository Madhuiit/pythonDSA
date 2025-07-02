class stack :
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def peek(self):
        return self.stack[-1] if self.stack else None
    


s = stack()
s.push(10)
s.push(20)
print(s.pop())   
print(s.peek())
    

