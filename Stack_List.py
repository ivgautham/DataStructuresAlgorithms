class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            return "Stack is empty!"
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return "Stack is empty!"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def length(self):
        return len(self.stack)
    
stack = Stack()
stack.push('1')
stack.push('2')
stack.push('3')

print("Stack: ", stack.stack)
print("Pop: ", stack.pop())
print("Peek: ", stack.peek())
print("Is stack empty or not?", stack.is_empty())
print("Lenght of the stack is: ", stack.length())
print("Stack: ", stack.stack)