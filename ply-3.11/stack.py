import sys 

class Stack: 

    def _int_(self): 
        self.stack = []
    
    def push(self, item): 
        self.stack.append(item)

    def pop(self): 
        if len(self.stack) >= 1: 
            return self.stack.pop() 
        return None 
    
    def peek(self): 
        return self.stack[len(self.stack) - 1] 
    
    def size(self): 
        return len(self.stack)
    
    def empty(self): 
        return len(self.stack) == 0